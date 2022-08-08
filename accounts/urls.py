from django.urls import path, re_path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_list, name="profile_list"),
    path('password_change/', views.password_change, name='password_change'),
    path('edit/', views.profile_edit, name='profile_edit'),
    # path('comment/new', views.profile_edit, name='profile_edit'),

    re_path(r'^usr/(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name="user_follow"),
    re_path(r'^usr/(?P<username>[\w.@+-]+)/unfollow/$', views.user_unfollow, name="user_unfollow"),
]