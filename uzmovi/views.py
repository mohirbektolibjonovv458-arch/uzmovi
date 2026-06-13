from django.shortcuts import render

# Create your views here.

def navigation(request):
    return render(request, 'navigation.html')

def footer(request):
    return render(request, 'footer.html')

def index(request):
    return render(request,"index.html")