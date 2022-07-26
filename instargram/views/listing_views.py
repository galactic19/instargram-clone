from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from instargram.models import Post, Tag
from instargram.forms import PostNewForm


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