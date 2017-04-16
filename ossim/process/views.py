from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
from . models import ProcessSchedAlg
from . utils import rr,sjf,srtf,fcfs,prepri,priority,multilevel

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
    if(pk=='1'):
        return render(request,'process/process.html')
    elif(pk=='2'):
        return render(request,'process/priority.html')
    elif(pk=='3'):
        return render(request,'process/multiLevel.html')

@csrf_exempt
def gateway(request):

    if request.method == 'POST':
        data = request.POST.get('value')
        data = json.loads(data)
        alg = request.POST.get('algo')
        alg=json.loads(alg)
        print(data)
        if(alg=="RR"):
        	tq = request.POST.get('tq')
        	tq = json.loads(tq)
        	result = rr(data,tq)
        elif(alg=="FCFS"):
            result = fcfs(data)
        elif(alg=="SRTF"):
            result = srtf(data)
        elif(alg=="SJF"):
            result = sjf(data)
        elif(alg=="PP"):
            result = prepri(data)
        elif(alg=="NPP"):
            result = priority(data)
        elif(alg=="MULTIQ"):
            tq = request.POST.get('tq')
            tq = json.loads(tq)
            table={'data':data,'tq':tq}
            queues,gantt,table = multilevel(table)
            result = {"queues":queues[:len(queues)-1], "gantt":gantt,"table":table}
        print(result)
    return JsonResponse(result)
