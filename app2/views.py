from django.shortcuts import render

# Create your views here.
def secondtemp(request):
    d={'a':32, 'b':45, 'c':78}
    return render(request, 'secondtemp.html',d)