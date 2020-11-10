from django.shortcuts import render,redirect
from .models import Number, Rank, EnrollTime
from django.contrib.auth.decorators import login_required
import datetime

import random
def makenumbers():
    num_li = ""
    for i in range(4):
        num = str(random.randint(1,9))
        num_li = num_li + num
    return num_li


# 메인(대기) 페이지
def waitboard(reqeust):
    now = datetime.datetime.now(datetime.timezone.utc)
    enrollTime = EnrollTime.objects.all()
    enrollTime = enrollTime[0]
    user = reqeust.user

    # 수강신청가능 데드라인
    deadline = enrollTime.EnrollTime + datetime.timedelta(minutes=3)
    print(now)
    print(enrollTime.EnrollTime)
    print(deadline)
    # 현재 시간과 다음 수강신청 시간 비교
    # 수강신청 가능 상태
    if now >= enrollTime.EnrollTime and now <= deadline:
        print("가능")
    # 수강신청 불가 상태
    else:
        
        # 이전 수강신청 번호 삭제
        pastnumbers = Number.objects.all()
        pastnumbers.delete()
        # 새로운 수강신청 시간 업데이트
        enrollTime.EnrollTime = enrollTime.EnrollTime + datetime.timedelta(minutes=6)
        enrollTime.save()
        # 새로운 수강신청 번호 생성
        for i in range(5):
            number = makenumbers()
            numModel = Number(applynumber=number)
            numModel.save()
        

    # 랜덤 생성된 숫자들 불러오기
    numbers =  Number.objects.all()
    # 시간을 정하고 그 시간이 지나면 서버에서 수강신청이 가능하도록 함 


    # 로그인 되어있다면
    if user.is_authenticated:
        # 순위 목록(rank_li)을 생성
        rank_li = {}
        # numbers = 만들어진 5개의 4자리수 숫자
        for number in numbers:
            # num_set = 수강신청 기록들의 집합
            # number를 통해 특정 4자리수 숫자의 수강신청 기록들의 목록을 생성
            num_set = Rank.objects.filter(number=number)
            # pk 값으로 정렬
            num_set.order_by("pk")
            # 로그인 된 유저가 수강신청했는지 검사하기 위해 
            mine = num_set.filter(user=user)
            # 순위 카운트는 1부터 시작
            rank = 1
            # 수강신청했는지 검사
            if mine.exists():
            #수강신청 했다면 mine이 존재 할 것이고 num_set 중에서 몇번째인지 카운트
                mine = mine[0]
                for num in num_set:
                    if num == mine:
                        break
                    else:
                        rank = rank + 1
                # number.applynumber = 현재 순위를 매기는 4자리수       
                rank_li[number.applynumber] = str(rank)
            else:
                rank_li[number.applynumber] = "수강 신청하지 않음"
        # 수강신청 4자리수 번호의 목록
        enrollnumbers = rank_li.keys()
        # 수강신청 4자리수 번호의 순위
        enrollranks = rank_li.values()
        context = {"numbers": numbers, "enrollnumbers":enrollnumbers, "enrollranks":enrollranks}
        return render(reqeust, "board/waitboard.html", context)
    else:
        context = {"numbers": numbers}
        return render(reqeust, "board/waitboard.html", context)

# 신청 페이지
@login_required
def enrollboard(reqeust):
    numbers =  Number.objects.all()
    context = {"numbers":numbers}
    return render(reqeust, "board/enrollboard.html", context)    

# 수강 신청하기
@login_required
def enroll(reqeust):
    # postnumber = 수강신청을 누른 번호 
    postnumber = reqeust.POST["number"]
    # 수강신청을 누른 번호의 외래키 적용을 위해 모델 객체로 변환 
    number = Number.objects.get(applynumber=postnumber)
    # 이 유저가 이미 수강신청 했는지를 알기 위해 user를 생성 
    user = reqeust.user
    #Rank 모델에 이 user가 이 number로 add한 객체가 있는지 검사
    check_rank = Rank.objects.filter(number=number, user=user)
    
    # 수강신청 하지 않았다면 = check_rank.exists() == False
    if not check_rank.exists():
        rank = Rank(number=number, user=user)
        rank.save()
        print("수강신청 되었습니다.")
    else:
        print("수강신청에 실패하였습니다.")
    # 수강 신청 후 리다이렉트
    return redirect("enrollboard")

