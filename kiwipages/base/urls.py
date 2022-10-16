from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('home/', views.home, name='home'),
    path('<int:contact_id>/', views.contact, name='contact'),
    path('settings/', views.settings, name='settings'),
    path('delete/<int:contact_id>/', views.delete, name='delete')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
