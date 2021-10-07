from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'detect/main.html')

def start(request):
    return render(request, 'detect/start.html')

def guide(request):
    return render(request, 'detect/guide.html')

def use(request):
    return render(request, 'detect/use.html')

def setting(request):
    return render(request, 'detect/setting.html')
