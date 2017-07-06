from django.shortcuts import render

# Create your views here.
from .forms import UserForm
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User


        
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            user = User.objects.filter(username = username)
            if len(user)>0:
                return render_to_response('register.html',{"errors":"用户名已存在"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render_to_response('register.html',{'errors':errors})
                password = password2
                email = uf.cleaned_data['email']
                #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username,'operation':"注册"})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})