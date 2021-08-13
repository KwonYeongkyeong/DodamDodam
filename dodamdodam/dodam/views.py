from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import answer
from .models import Picture

# from .static.stt import main
# from .static.tts import run_quickstart, play

from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request, 'home.html')

def last(request, id):
    take = get_object_or_404(answer,pk=id)
    return render(request, 'last.html',{'take':take})

def mypage(request):
    return render(request, 'mypage.html')

def picture(request, id):
    take = get_object_or_404(answer,pk=id)
    return render(request, 'picture.html', {'take':take})

def voice(request,id):
    take = get_object_or_404(answer,pk=id)
    return render(request, 'voice.html',{'take':take, 'state':'next'})

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

def result(request, id):
    take = get_object_or_404(answer,pk=id)
    return render(request, 'result.html', {'take':take})

def setQ(request):
    if(request.method == 'POST'):
        take = answer()
        take.pub_date = timezone.datetime.now()
        take.q1 = "오늘은 기분이 어때? 왜 그런 기분이야?"
        if request.POST["ans1"]:
            take.q1 = request.POST["ans1"]
        take.q2 = "오늘 기뻤던 일은 뭐야?"
        if request.POST["ans2"]:
            take.q2 = request.POST["ans2"]
        take.q3 = "오늘 슬펐던 일은 뭐야?"
        if request.POST["ans3"]:
            take.q3 = request.POST["ans3"]
        take.picture = "집"
        if request.POST["ans4"]:
            take.picture = request.POST["ans4"]
        take.writer = request.user
        take.save()
    return render(request, "home.html", {'take':take})

def picture(request,id):
    take = get_object_or_404(answer,pk=id)
    return render(request, 'picture.html', {'take': take})

def diary(request, id):
    take = get_object_or_404(answer,pk=id)
    return render(request, "diary.html", {'take': take})

def record(request,id):
    take = get_object_or_404(answer,pk=id)
    # run_quickstart(take.q1, take.q2, take.q3) #TTS
    # play("output.mp3",True)
    # take.ans = main() #STT
    take.save()
    return render(request, "voice.html",{'take':take})

def nextVoice(request,id):
    take = get_object_or_404(answer,pk=id)
    # play("output2.mp3",False)
    return render(request, "voice.html",{'take':take, 'state':'final'})

def finalVoice(request,id):
    take = get_object_or_404(answer,pk=id)
    # play("output3.mp3",False)
    return render(request, "voice.html",{'take':take})

def drawing(request):
    draw = Picture()
    draw.draw = request.POST['image']
    draw.save()
    return redirect("/dodam/result/")
