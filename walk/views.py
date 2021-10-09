from django.shortcuts import render
from .models import Park

# Create your views here.
def menu(request):
    parks = Park.objects.all()
    return render(request, 'walk/menu.html', {"parks": parks})