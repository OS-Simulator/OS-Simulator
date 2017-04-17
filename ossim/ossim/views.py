from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'ossim/index.html')

def matindex(request):
    return render(request, 'mat/mainindex.html')
