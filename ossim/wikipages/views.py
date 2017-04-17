from django.shortcuts import render

# Create your views here.
def bankers(request):
    return render(request, 'wikipages/bankers.html')

def disk(request):
    return render(request, 'wikipages/disk.html')

def mem(request):
    return render(request, 'wikipages/Mem.html')

def pra(request):
    return render(request, 'wikipages/PRA.html')

def process(request):
    return render(request, 'wikipages/Process.html')

def semaphore(request):
    return render(request, 'wikipages/Semaphore.html')

def socket(request):
    return render(request, 'wikipages/Socket.html')
