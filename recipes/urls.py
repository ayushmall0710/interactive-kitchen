from django.urls import path
from . import views

urlpatterns = [
    path('suggest/', views.suggest_recipe, name='suggest_recipe'),
]