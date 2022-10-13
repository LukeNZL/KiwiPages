from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('settings/', views.settings, name='settings')

]