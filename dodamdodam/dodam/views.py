from django.http import request
from django.shortcuts import redirect, render
from .models import answer
from .models import Picture

# from .static.stt import main
# from .static.tts import run_quickstart

from django.contrib.auth.models import User
from django.contrib import auth
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

def consult(request):
    return render(request, 'consult.html')

def setquest(request):
    return render(request, "setquest.html")

def join(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                request.POST["username"], password=request.POST["password1"]
            )
            # auth.login(request, user)
            return redirect("/dodam/login/")  # 뭐넣어야하는지 고민해보자
    return render(request, "join.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/dodam/consult/")
        else:
            return render(
                request, "login.html", {"error": "username or password is incorrect"}
            )
    else:
        return render(request, "login.html")

def result(request):
    return render(request, "result.html")

def setQ(request):
    if(request.method == 'POST'):
        take = answer()
        if request.POST['ans1'] == 1:
            take.q1 = request.POST['ans1']
        else:
            take.q1 = "오늘은 기분이 어때? 왜 그런 기분이야?"
        
        if request.POST['ans2'] == 1:
            take.q2 = request.POST['ans2']
        else:
            take.q2 = "오늘 기뻤던 일은 뭐야?"

        if request.POST['ans3'] == 1:
            take.q3 = request.POST['ans1']
        else:
            take.q3 = "오늘 슬펐던 일은 뭐야?"
        
        if request.POST['ans4'] == 1:
            take.picture = request.POST['ans4']
        else:
            take.picture = "집"

        take.save()

    return render(request, "home.html")

def picture(request):
    take = answer.objects
    return render(request, 'picture.html', {'take': take})

def diary(request):
    return render(request, "diary.html")

def record(request):
#    run_quickstart() #TTS
#    main() #STT
    return render(request, "voice.html")

def drawing(request):
    draw = Picture()
    draw.draw = request.POST['image']
    draw.save()
    return redirect("/dodam/result/")
