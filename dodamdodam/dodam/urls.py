from dodam import views
from django.urls import path
#TEMPLATE TAGGING
app_name = 'dodam_app'

urlpatterns= [
    path('last<str:id>',views.last,name='last'),
    path('mypage/',views.mypage,name='mypage'),
    path('picture<str:id>',views.picture,name='picture'),
    path('voice<str:id>',views.voice,name='voice'),
    path('consult/', views.consult,name='consult'),
    path('setquest/', views.setquest,name='setquest'),
    path('join/',views.join,name='join'),
    path('home/',views.home,name="home"),
    path('result<str:id>', views.result,name='result'),
    path('diary<str:id>', views.diary, name="diary"),
    path("record<str:id>", views.record, name="record"),
    path("login/", views.login, name="login"),
    path("nextVoice<str:id>", views.nextVoice, name="nextVoice"),
    path("finalVoice<str:id>", views.finalVoice, name="finalVoice"),
]