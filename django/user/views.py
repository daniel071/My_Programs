from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserAccount


def userView(request):
    all_todo_items = UserAccount.objects.all()
    return render(request, 'users.html',
                  {'all_items': all_todo_items})


def addUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    new_item = UserAccount(username=username, password=password, email=email)
    new_item.save()
    return HttpResponseRedirect('/users/')
