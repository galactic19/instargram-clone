from django.urls import path
from django.contrib.auth.validators import UnicodeUsernameValidator
from .views import creating_views, listing_views, userpage_views

app_name='instargram'

urlpatterns = [
    path('', listing_views.post_list, name='post_list'),
    path('userpage/<str:username>/', userpage_views.user_page, name="user_page"),
    path('post_new', creating_views.post_new, name="post_new"),
    path('post/', listing_views.post_list, name='post_list'),
    path('post/<int:pk>/', listing_views.post_detail, name="post_detail"),
    path('edit/<int:pk>/', creating_views.post_edit, name="post_edit"),
    path('delete/<int:pk>/', creating_views.PostDeleteView.as_view(), name="post_delete"),
    path('tags/<int:pk>/', listing_views.tag_list, name="tag_list"),
]
