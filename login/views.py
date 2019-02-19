from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models
# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #插入数据库
        models.UserInfo.objects.create(username=username, password=password)
    #获取数据库中userinfo表所有信息
    user_list = models.UserInfo.objects.all()
    #返回数据到index页面
    return render(request, 'index.html', {'data': user_list})

