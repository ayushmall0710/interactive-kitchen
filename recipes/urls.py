from django.urls import path
from . import views

urlpatterns = [
    path('suggest/', views.suggest_recipe, name='suggest_recipe'),
    path('save/', views.save_recipe, name='save_recipe' ),
    path('list/', views.save_recipe, name='list_recipes' ),
]