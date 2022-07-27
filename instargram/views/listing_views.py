from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from instargram.models import Post, Tag


@login_required
def post_index(request):
    # 팔로우한 사람의 게시물을 가져옴.
    posts = Post.objects.all()\
        .filter(Q(author=get_user(request)) | Q(author__in=get_user(request).following_set.all()))[:6]

    # 팔로우 추천
    suggested_user_list = get_user_model().objects.exclude(pk=get_user(request).pk)\
                            .exclude(pk__in=get_user(request).following_set.all())
    # 맞팔.
    followers_user = get_user_model().objects.filter(following=get_user(request).pk)\
                                                .filter(follower=get_user(request).pk)
    context = {'suggested_user_list': suggested_user_list, 'followers_user':followers_user, 'object_list': posts}
    return render(request, 'instargram/index.html', context)


@login_required
def post_list(request):
    post_list = Post.objects.all()
    context = {'object_list':post_list}
    return render(request, 'instargram/post_list.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    who_is = request.user.is_authenticated and request.user == post.author
    context = {'post_list': post, 'who_is':who_is}
    return render(request, 'instargram/post_detail.html', context)


def tag_list(req, pk):
    context = {'object_list': get_object_or_404(Tag, pk=pk).post_set.all()}
    return render(req, 'instargram/post_list.html', context)