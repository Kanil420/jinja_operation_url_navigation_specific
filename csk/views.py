from django.shortcuts import render

# Create your views here.
def msd(request):
    return render(request,'msd.html')
def king(request):
    return render(request,'rcb.html')
