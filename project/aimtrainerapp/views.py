from django.shortcuts import render

def home(request):
    return render(request, 'aimtrainerapp/home.html')

def game(request):
    return render(request, 'aimtrainerapp/game.html')