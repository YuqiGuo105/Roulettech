from django.urls import path
from . import views
from .views import get_presigned_url, generate_recipe, recipe_list, recipe_detail

urlpatterns = [
    path('presigned-url/', get_presigned_url, name='get_presigned_url'),
    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/<str:pk>/', recipe_detail, name='recipe-detail'),
    path('generate-recipe/', generate_recipe, name='generate-recipe'),
]
