from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('/<int:pk>/', views.blog_detail, name='blog_detail'),
]
