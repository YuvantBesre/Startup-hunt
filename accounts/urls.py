
from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.SignUpPage, name='Sign-up'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.Logout, name='logout')
]
