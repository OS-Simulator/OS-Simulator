from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
from . models import DiskSchedAlg
from . utils import cscan

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
        print(data)
        result = cscan(data)
        print(result)
    return JsonResponse({'output':result})
