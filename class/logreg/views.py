from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.shortcuts import redirect
  
def regist(req):                         #注册
        if req.method == 'POST':
                uf = UserForm(req.POST)
                if uf.is_valid():
                        username = uf.cleaned_data['username']
                        password = uf.cleaned_data['password']
                        User.objects.create(username = username ,password = password)
                        return HttpResponseRedirect('/login/')   #跳转到那个路径
        else:
                uf = UserForm()
        return render_to_response('regist.html',{'uf':uf})
def login(req):                           #登录
        if req.method == 'POST':
                uf = UserForm(req.POST)
                if uf.is_valid():
                        username = uf.cleaned_data['username']
                        password = uf.cleaned_data['password']
                        users = User.objects.filter(username = username ,password = password)       #数据库搜素，如果users对象不为空，代表搜索成功
                        if users:
                                response = HttpResponseRedirect('/index/')
                                #生成response对象设置cookie，cookie为字典
                                response.set_cookie('username',username,3600)
                                return response     #把username传给下个页面
                        else:
                                return HttpResponseRedirect('/login/')
        else:
                uf = UserForm()
        return render_to_response('login.html',{'uf':uf})
def index(req):
        username = req.COOKIES.get('username','')   #读取cookie
        return render_to_response('index.html',{'username':username})
def logout(req):
        response = HttpResponse('logout')
        response.delete_cookie('username')
        return response