from dodam import views
from django.urls import path
#TEMPLATE TAGGING
app_name = 'dodam_app'

urlpatterns= [
    path('last/',views.last,name='last'),
    path('mypage/',views.mypage,name='mypage'),
    path('picture/',views.picture,name='picture'),
    path('voice/',views.voice,name='voice'),
]