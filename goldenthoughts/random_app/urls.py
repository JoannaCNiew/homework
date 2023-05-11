from django.urls import path
from random_app import views

urlpatterns = [
    path('random', views.random_view)
]