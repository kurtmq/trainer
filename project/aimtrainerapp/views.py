from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Score

def home(request):
    return render(request, 'aimtrainerapp/home.html')

def game(request):
    return render(request, 'aimtrainerapp/game.html')

def save_score(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        score = request.POST.get('score')
        
        if name and score:
            Score.objects.create(
                name=name,
                score=int(score)
            )
            
            if request.POST.get('action') == 'save_and_play':
                return redirect('game')
            else:
                return redirect('home')
                
    return redirect('home')

def leaderboard(request):
    # Get all scores ordered by score (ordering is already set in model Meta)
    scores = Score.objects.all()
    return render(request, 'aimtrainerapp/leaderboard.html', {'scores': scores})