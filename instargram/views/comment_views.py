
'''
    코멘트에 대해서 이 파일에서 처리한다.
'''

from django.contrib.auth import get_user
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from ..forms import CommentNewForm
from ..models import Post


def comment_new(request, post_pk):
    if request.method == "POST":
        form = CommentNewForm(request.POST, request.FILES)
        post = get_object_or_404(Post, pk=post_pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = get_user(request)
            comment.post_id = post
            comment.save()
            return redirect(comment.post_id)
    else:
        redirect_url = request.headers.get('HTTP_REFERER', '/')
        return redirect(redirect_url)