from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostNewForm


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostNewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = request.user
            post = form.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, '포스트 등록이 완료 되었습니다.')
            return redirect(post)
    else:
        form = PostNewForm()
    context = {'form': form}
    return render(request, 'instargram/post_form.html', context)


@login_required
def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'instargram/post_list.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    context = {'post_list': post}
    return render(request, 'instargram/post_detail.html', context)