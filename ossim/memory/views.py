from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
from . models import MemSchedAlg
from . utils import fifo as ff

def home(request):
    algos = MemSchedAlg.objects.all()
    context = {'algos': algos}
    return render(request, 'memory/index.html',context = context)

def detail(request,pk):
    alg = get_object_or_404(MemSchedAlg, pk=pk)
    context = {'alg':alg,
               }
    return render(request,'memory/detail.html',context=context)

def demo(request,pk):
    return render(request,'memory/page.html')

@csrf_exempt
def fifo(request):

    if request.method == 'POST':
        data = request.POST.get('requests')
        requests = json.loads(data)
        data = request.POST.get('size')
        size = json.loads(data)

        data = {'requests': requests, 'size':size}
        print(data)
        print("Reached")
        result = ff(data)
        print(result)
    return JsonResponse(result)
