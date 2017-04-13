from django.shortcuts import render

# Create your views here.
from . models import SynchroAlg


def home(request):
    algos = SynchroAlg.objects.all()
    context = {'algos': algos}
    return render(request, 'synchro/index.html',context = context)

def detail(request,pk):
    alg = get_object_or_404(ProcessSchedAlg, pk=pk)
    context = {'alg':alg,
               }
    return render(request,'synchro/detail.html',context=context)
