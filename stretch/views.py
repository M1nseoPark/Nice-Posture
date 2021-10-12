from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'stretch/menu.html')

def posture(request):
    return render(request, 'stretch/posture.html')

def neck_shoulder(request):
    return render(request, 'stretch/neck_shoulder.html')

def waist(request):
    return render(request, 'stretch/waist.html')

def knee(request):
    return render(request, 'stretch/knee.html')

def back(request):
    return render(request, 'stretch/back.html')

def body(request):
    return render(request, 'stretch/body.html')

def detail(request):
    return render(request, 'stretch/detail.html')