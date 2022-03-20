from django.urls import path
from .views import *

urlpatterns = [
    path("",inicio,name='inicio'),
    path("contactame/",contactame,name='contactame'),
    path("crearpost/",crearpost,name='crearpost'),
    path("buscarpost/",buscarpost,name='buscarpost'),
    path("crearusuario/",crearusuario,name= 'crearusuario'),
]
