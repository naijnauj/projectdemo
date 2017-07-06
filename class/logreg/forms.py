from django import forms
from .models import User
#  class ArticleForm(forms.Form):
 #     title = forms.CharField(label="标题",max_length=100)
  #    ontent = forms.CharField(label="内容",max_length=10000)
class UserForm(forms.ModelForm):
    username = forms.CharField(label='用户名',max_length=30)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())