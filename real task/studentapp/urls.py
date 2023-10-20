from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('new/', views.new_page, name='new'),
    path('add/', views.add_customer, name='customer'),
    path('get_courses/', views.get_courses, name='get_courses'),

]
