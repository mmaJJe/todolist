from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.mypage, name="mypage"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('sign_up', views.signup, name="signup"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
]
