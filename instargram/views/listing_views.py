import datetime

from django.contrib import messages
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from instargram.models import Post, Tag
from ..forms import CommentNewForm


@login_required
def post_index(request):
    # 시간에 관련한 설정 / 현재시간에서 3일의 시간을 뺌. 게시물을 작성하고 3일이 지나면 게시물이 나타나지 않음
    timesince = timezone.now() - datetime.timedelta(days=3)

    # 팔로우한 사람의 게시물을 가져옴.
    posts = Post.objects.all()\
        .filter(Q(author=get_user(request)) | Q(author__in=get_user(request).following_set.all()))\
        .filter(created_at__gt=timesince)\
        .filter(is_used=True)

    # 팔로우 추천
    suggested_user_list = get_user_model().objects.exclude(pk=get_user(request).pk)\
                            .exclude(pk__in=get_user(request).following_set.all())
    # 맞팔.
    followers_user = get_user_model().objects.filter(following=get_user(request).pk)\
                                            .filter(follower=get_user(request).pk)
    context = {
                'suggested_user_list': suggested_user_list,
                'followers_user': followers_user,
                'object_list': posts,
                'form': CommentNewForm()
               }
    return render(request, 'instargram/index.html', context)


@login_required
def post_list(request):
    post = Post.objects.all()
    context = {'object_list': post}
    return render(request, 'instargram/post_list.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    who_is = request.user.is_authenticated and request.user == post.author
    context = {'post_list': post, 'who_is':who_is}
    return render(request, 'instargram/post_detail.html', context)


@login_required
def post_like(request, pk):
    '''
        포스트 like 를 처리해줄 함수.
        post like 를 확인하여 좋아요, 좋아요 취소를 처리함.
    '''
    post = get_object_or_404(Post, pk=pk)
    like_check = post.like_user_set.filter(pk=get_user(request).pk)
    if like_check:
        post.like_user_set.remove(get_user(request))
        messages.info(request, f'{post.author} 포스트에 좋아요를 취소 했습니다.')
    else:
        post.like_user_set.add(get_user(request))
        messages.success(request, f'{post.author} 포스트에 좋아요를 완료 했습니다.')

    redirect_url = request.headers.get('HTTP_REFERER', '/')
    return redirect(redirect_url)


def tag_list(req, pk):
    form = CommentNewForm()
    context = {'object_list': get_object_or_404(Tag, pk=pk).post_set.all(), 'form': form}
    return render(req, 'instargram/post_list.html', context)