from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator
from .views import creating_views, listing_views, userpage_views, comment_views

app_name='instargram'

urlpatterns = [
    path('', listing_views.post_index, name='post_index'),
    path('post_new', creating_views.post_new, name="post_new"),
    path('post/', listing_views.post_list, name='post_list'),
    path('post/<int:pk>/', listing_views.post_detail, name="post_detail"),
    path('post/<int:pk>/like/', listing_views.post_like, name="post_like"),
    # path('post/<int:pk>/unlike/', listing_views.post_unlike, name="post_unlike"),
    path('edit/<int:pk>/', creating_views.post_edit, name="post_edit"),
    path('delete/<int:pk>/', creating_views.PostDeleteView.as_view(), name="post_delete"),
    path('comment_new/<int:post_pk>/', comment_views.comment_new, name="comment_new"),
    path('tags/<int:pk>/', listing_views.tag_list, name="tag_list"),
    re_path(r'^usr/(?P<username>[\w.@+-]+)/$', userpage_views.user_page, name="user_page"),
]
