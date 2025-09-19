#app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu),
    path('ping/', views.ping),
    path('sum/', views.sum),

]

