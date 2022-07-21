from django.urls import path
from . import views


app_name='instargram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new', views.post_new, name="post_new"),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name="post_detail"),
]
