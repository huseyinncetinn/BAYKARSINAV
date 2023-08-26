from django.urls import path
from .views import *


urlpatterns=[
    path('', index , name='index'),
    path('login/' , login , name='login'),
    path('register/' , register , name='register'),
    path('logout/' , logout_request , name='logout'),
    path('ihadetay/<str:ihaid>' , ihaDetay , name='ihaDetay'),
    path('profil/' , profil , name='profil'),
    path('kiralama/' , kiralama , name='kiralama'),
    path('delete/<int:id>' , deleteIha , name='deleteIha')

]