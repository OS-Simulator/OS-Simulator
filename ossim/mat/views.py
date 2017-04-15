from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
import json

def home_page(request):
    return render(request, 'mat/index.html')

def mat_mft_get_data(request):
    variables = ['total_memory', 'no_of_blocks']
    submitted = True
    context = {}
    block_size = [0,1,2,3,4,5,6,7,8,0,1,1,1,1,1]
    context['invalid_data'] = False
    for x in variables:
        submitted = request.POST.get(x,False)
        if submitted is False:
            print("Hello")
            break
        else:
            try:
                context[x] = int(request.POST.get(x))
            except ValueError:
                context['invalid_data'] = True
                break

    if context['invalid_data'] is False and submitted:
        for i in range(1, context['no_of_blocks']+1):
            block_size[i] = request.POST.get('block_size_' + str(i))
        context['block_size'] = json.dumps(block_size)

    if submitted is False or context['invalid_data'] is True:
        return render(request, 'mat/mft/get_data.html', context)
    else:
        return render(request, 'mat/mft/show_demo.html', context)

def mat_mvt_get_data(request):
    if request.POST:
        context = {
            'totalMemory' : request.POST['total_memory'],
            'inputMemory' : request.POST['input_memory']
        }
        return render(request, 'mat/mvt/show_demo.html', context)
    return render(request, 'mat/mvt/get_data.html')

