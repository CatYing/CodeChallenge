# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
import datetime
from models import *


@login_required(login_url=reverse_lazy('login'))
def start(request):
    return render(request, 'start.html', {'user': request.user})


def index(request):
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'index.html', {'user': user})


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('start'))

    state = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        realname = request.POST.get('realname', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            state = 'exist'
        else:
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()
            new_my_user = MyUser(user=new_user, realname=realname, start_time=datetime.datetime.now())
            new_my_user.save()
            state = 'success'

    content = {'state': state, 'user': None}
    return render(request, 'signup.html', content)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('start'))

    state = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('start'))
        else:
            state = 'error'
    content = {'state': state, 'user': None}
    return render(request, 'login.html', content)


@login_required(login_url=reverse_lazy('login'))
def judge(request, answer):
    myuser = MyUser.objects.filter(user=request.user)[0]
    solution = Solution.objects.filter(url=answer)
    if solution and solution[0].num - myuser.pass_num == 1:
        myuser.pass_num += 1
        myuser.end_time = datetime.datetime.now()
        myuser.save()
        return render(request, answer + '.html')
    elif solution and solution[0].num - myuser.pass_num < 1:
        return render(request, answer + '.html')
    else:
        return HttpResponseRedirect('/wrong/')


@login_required(login_url=reverse_lazy('login'))
def wrong(request):
    return HttpResponse("答案错误或非法操作")


@login_required(login_url=reverse_lazy('login'))
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('signup'))