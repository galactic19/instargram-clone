from django.urls import path, reverse_lazy
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_list, name="profile_list"),
    path('password_change/', views.passord_change, name='password_change'),
    path('edit/', views.profile_edit, name='profile_edit'),
]


