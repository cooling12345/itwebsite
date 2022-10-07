from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def board(request):
    return render(request, 'website/board.html')

def swipe(request):
    return render(request, 'website/swipe.html')

def music(request):
    return render(request, 'website/music.html')