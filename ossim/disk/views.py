from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
from . models import DiskSchedAlg
from . utils import cscan,clook, scan,look,sstf,fcfs

def home(request):
    algos = DiskSchedAlg.objects.all()
    context = {'algos': algos}
    return render(request, 'disk/index.html',context = context)

def detail(request,pk):
    alg = get_object_or_404(DiskSchedAlg, pk=pk)
    context = {'alg':alg,
               }
    return render(request,'disk/detail.html',context=context)

def demo(request):
    return render(request,'disk/disk.html')

@csrf_exempt
def gateway(request):

    if request.method == 'POST':
        data = request.POST.get('value')
        data = json.loads(data)
        alg = request.POST.get('algo')
        alg=json.loads(alg)
        print(data)
        if(alg=="CSCAN"):
            result = cscan(data)
        elif(alg=="CLOOK"):
            result = clook(data)
        elif(alg=="FCFS"):
            result = fcfs(data)
        elif(alg=="SCAN"):
            result = scan(data)
        elif(alg=="LOOK"):
            result = look(data)
        elif(alg=="SSTF"):
            result = sstf(data)

        print(result)
    return JsonResponse({'output':result})
