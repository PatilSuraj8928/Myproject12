from django.shortcuts import render

# Create your views here.
def firsttemp(request):
    d={'a':12, 'b':43, 'c':34}
    return render(request, 'firsttemp.html',d)