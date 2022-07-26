from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, get_user
from ..models import Post

'''
    UserPage 생성하여 관리.
'''

def user_page(request, username):
    user_page = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=user_page.pk)
    is_user_check = user_page.username == get_user(request).username
    return render(request, 'instargram/user_page.html', 
                  {'user_page':user_page,
                   'post_list': post_list,
                   'is_user_check': is_user_check,
                   })