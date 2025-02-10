# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('inquiry/', views.inquiry_view, name='inquiry'),
    path('founder/', views.about_founder, name='founder'),  
    path('success/', views.success, name='success'),
]
