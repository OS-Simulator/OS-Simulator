from django.shortcuts import render
from .backend.status import Status
from .backend.status2 import Status2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .backend.backendInterface import Tree
from .backend.backendInterface import Two
import json

ob = []
ob2 = []
# Create your views here.
def home(request):
    return render(request, 'filesystem/home.html')

@csrf_exempt
def tree(request, choice):
    global ob
    ob = Tree()
    Status.choice = choice
    Status.flag = 0
    Status.path = ['root']
    Status.filelis = []
    dictionary = {'filelis' : Status.filelis, 'path' : Status.path, 'flag' : Status.flag}
    return render(request, 'filesystem/tree.html', {"dictionary" : dictionary})

@csrf_exempt
def single(request, choice):
    global ob
    ob = Tree()
    Status.choice = choice
    Status.flag = 0
    Status.path = ['root']
    Status.filelis = []
    dictionary = {'filelis' : Status.filelis, 'path' : Status.path, 'flag' : Status.flag}
    return render(request, 'filesystem/single.html', {"dictionary" : dictionary})

@csrf_exempt
def two(request, choice):
    global ob2
    ob2 = Two()
    Status2.choice = choice
    Status2.flag = 0
    Status2.flag1 = 0
    Status2.flag2 = 0
    Status2.path = ['root']
    Status2.filelis = []
    dictionary = {'filelis' : Status2.filelis, 'path' : Status2.path, 'flag' : Status2.flag, 'flag1' : Status2.flag1, 'flag2' : Status2.flag2}
    return render(request, 'filesystem/two.html', {"dictionary" : dictionary})

@csrf_exempt
def process(request):
    path = request.POST.getlist('path[]')
    command = request.POST.get('command')
    ob.passCmd(path, command)
    dictionary = {'filelis' : Status.filelis, 'path' : Status.path, 'flag' : Status.flag}
    return HttpResponse(json.dumps({"dictionary" : dictionary}), content_type="application/json")

@csrf_exempt
def process2(request):
    path = request.POST.getlist('path[]')
    command = request.POST.get('command')
    ob2.passCmd(path, command)
    dictionary = {'filelis' : Status2.filelis, 'path' : Status2.path, 'flag' : Status2.flag, 'flag1' : Status2.flag1, 'flag2' : Status2.flag2}
    return HttpResponse(json.dumps({"dictionary" : dictionary}), content_type="application/json")
