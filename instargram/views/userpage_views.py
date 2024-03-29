from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, get_user

'''
    UserPage 생성하여 관리.
'''


def user_page(request, username):
    usr_page = get_object_or_404(get_user_model(), username=username, is_active=True)
    is_user_check = usr_page.username == get_user(request).username
    if get_user(request).is_authenticated:
        is_follow = get_user(request).following_set.filter(pk=usr_page.pk).exists()
    else:
        is_follow = False
    post_cnt = usr_page.my_post_set.count()
    context = {
                'user_page': usr_page,
                'is_user_check': is_user_check,
                'post_cnt': post_cnt,
                'is_follow': is_follow
               }
    return render(request, 'instargram/user_page.html', context)