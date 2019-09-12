
from django import forms
from django.core.exceptions import ValidationError

from userapp.widgets import SendEmailButton
from .models import OneGuoUser


class UsersForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           required=True,
                           error_messages={
                               'required': '账号不能为空',
                               'max_length': '账户不能超过10个字符',
                           })

    password = forms.CharField(widget=forms.PasswordInput,
                               label='密码',
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不得少于6位'
                               })

    class Meta:
        model = OneGuoUser
        fields = ('name', 'password', 'phone', 'img', 'use_level', 'email')
        error_messages = {
            'email': {
                'required': '邮箱不能为空'
            }
        }

    def is_valid(self):
        return super().is_valid()


class ResgisterForm(forms.Form):
    gender = (
        ('man', "男"),
        ('women', "女"),
    )
    name = forms.CharField(label="用户名",
                           max_length=128,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码",
                               max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别',
                            choices=gender)

    class Meta:
        model = OneGuoUser
        fields = ('name', 'password', 'email', 'sex')
