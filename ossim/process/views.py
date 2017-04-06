from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
from . models import ProcessSchedAlg
from . utils import rr

def home(request):
    algos = ProcessSchedAlg.objects.all()
    context = {'algos': algos}
    return render(request, 'process/index.html',context = context)

def detail(request,pk):
    alg = get_object_or_404(ProcessSchedAlg, pk=pk)
    context = {'alg':alg,
               }
    return render(request,'process/detail.html',context=context)

def demo(request,pk):
    return render(request,'process/process.html')

@csrf_exempt
def gateway(request):

    if request.method == 'POST':
        data = request.POST.get('value')
        data = json.loads(data)
        alg = request.POST.get('algo')
        alg=json.loads(alg)

        if(alg=="RR"):
            result = rr(data)
        elif(alg=="FCFS"):
            result = fcfs(data)
        elif(alg=="SRTF"):
            result = srtf(data):

    return JsonResponse(result)
