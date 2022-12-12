from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Todolist

# Create your views here.

def index(response):
    list = Todolist.objects.all()
    p = {
        "list": list,
    }
    return render(response, 'main/index.html', p)

def add_view(response):
    return render(response, 'main/add.html', {})

def addList(response):
    list = Todolist()

    if response.method == 'POST':
        listname = response.POST['listname']
        listtitle = response.POST['listtitle']
        timefrom = response.POST['timefrom']
        timeto = response.POST['timeto']

        list.name = listname
        list.title = listtitle
        list.timefrom = timefrom
        list.timeto = timeto
        list.save()

        return redirect('/')

    return render(response, 'main/index.html', {})

def deleteList(response, pk):
    list = Todolist.objects.get(id = pk)
    list.delete()
   
    return redirect('/')



