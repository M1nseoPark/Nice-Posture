from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'walk/menu.html')

def beginner(request):
    return render(request, 'walk/beginner.html')

def intermediate(request):
    return render(request, 'walk/intermediate.html')

def senior(request):
    return render(request, 'walk/senior.html')