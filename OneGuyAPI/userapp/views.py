from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.goods import OneGuoUserSerializer

from .forms import ResgisterForm
from userapp.models import OneGuoUser


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error_msg = '用户名或密码错误'
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        if all((name, password)):
            user_qs = OneGuoUser.objects.filter(name=name)
            if user_qs.exists():
                user = user_qs.first()
                if password == user.password:
                    request.session['login_user'] = {
                        'id': user.name,
                        'name': user.password
                    }

                    return redirect('/')
            else:
                error_msg = '用户名不存在，请先注册'

        return render(request, 'login.html', locals())



def logout(request):
    request.session.clear()
    # request.session.flush()
    resp = HttpResponse('注销成功')
    resp.delete_cookie('token')
    return resp


def register(request):
    if request.session.get('is_login', None):
        # 限制重复登录
        return redirect('index.html')
    if request.method == 'POST':
        # post请求
        message = '请检查填写的内容'
        name = request.POST.get('name')
        password = request.POST.get('password')

        email = request.POST.get('email')
        sex = request.POST.get('sex')

        user_name = OneGuoUser.objects.filter(name=name).first()

        if user_name:
            message = '用户名已经存在'
            return render(request, 'register.html', locals())

        user_email = OneGuoUser.objects.filter(email=email).first()
        if user_name:
            message = '邮箱已经注册'
            return render(request, 'register.html', locals())

        new_user = OneGuoUser.objects.create()
        new_user.name = name
        new_user.password = password
        new_user.email = email
        new_user.sex = sex
        new_user.save()
        return redirect('user:login')  # 自动跳转到登录页面

    return render(request, 'register.html', locals())
