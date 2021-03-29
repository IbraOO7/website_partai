from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.daftar, name='daftar'),
    path('tambahdaftar', views.tambahdaftar, name='tambahdaftar')
]
