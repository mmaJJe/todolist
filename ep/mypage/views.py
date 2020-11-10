from django.shortcuts import render
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mypage(request):
    return render(request, "mypage/mypage.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password == cpassword:
            user = User.object.create_user(
                username=username, password=password
            )
            login(request, user)
        else:
            return render(request, "mypage/signup.html")
    else:
        return render(request, "mypage/signup.html")