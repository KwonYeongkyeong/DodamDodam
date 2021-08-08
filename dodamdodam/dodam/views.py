from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def last(request):
    return render(request, 'last.html')

def mypage(request):
    return render(request, 'mypage.html')

def picture(request):
    return render(request, 'picture.html')

def voice(request):
    return render(request, 'voice.html')