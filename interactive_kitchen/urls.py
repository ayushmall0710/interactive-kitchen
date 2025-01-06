"""
URL configuration for interactive_kitchen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views as inventory_views
from users import views as user_views
from recipes import views as recipe_views
from users.views import RegisterView, LoginView, LogoutView, UserViewSet

# Router for DRF
router = DefaultRouter()
router.register(r'inventory', inventory_views.InventoryViewSet, basename='inventory')
# router.register(r'receipts', inventory_views.ReceiptViewSet, basename='receipts')
# router.register(r'profiles', user_views.ProfileViewSet, basename='profiles')
router.register(r'recipes', recipe_views.RecipeSuggestionViewSet, basename='recipes')
router.register(r'users', UserViewSet, basename='users')

# Root view
def root_view(request):
    return JsonResponse({"message": "Welcome to the Interactive Kitchen API!"})

urlpatterns = [
    path('', root_view, name='root'),  # Add a root view
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/', include('rest_framework.urls')),
]
