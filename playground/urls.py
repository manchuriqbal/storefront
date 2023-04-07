from django.urls import path
from playground import views

urlpatterns = [
    path('', views.playground, name="playground"),
]