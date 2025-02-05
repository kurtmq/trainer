from django.shortcuts import render

def home(request):
    return render(request, 'aimtrainerapp/home.html')