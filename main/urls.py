from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
]
