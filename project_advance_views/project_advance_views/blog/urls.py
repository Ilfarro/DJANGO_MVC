from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('input_post/', views.input_post, name='input_post'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
]