from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('testimonial/', views.testimonial_list, name='testimonial-list'),
]
