
from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.CreateProduct, name='create'),
    path('<int:company_id>', views.FullProductPage, name='FullProductPage'),
    path('<int:company_id>/upvote', views.upvote, name='upvote'),
    path('<int:company_id>/upvoteAtHome', views.upvoteAtHome, name='upvoteAtHome'),
]
