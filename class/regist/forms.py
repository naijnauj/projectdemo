from django import forms
from .models import User

 #定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')