from django.urls import path
from . import views
from .views import get_presigned_url

urlpatterns = [
    path('presigned-url/', get_presigned_url, name='get_presigned_url'),
    path('recipes/', views.recipe_list, name='recipe-list'),
    path('recipes/<str:pk>/', views.recipe_detail, name='recipe-detail'),
]
