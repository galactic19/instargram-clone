from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from instargram.models import Post, Tag
from instargram.forms import PostNewForm


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


def post_edit(request, pk):
    '''
        user 로그인과 , 글쓴이 유저가 맞는지를 확인한 다음. 
        update 진행 form 은 PostNewForm form을 사용
    '''
    post = get_object_or_404(Post, pk=pk)
    
    if request.user.is_authenticated and request.user == post.author:
        if request.method == 'POST':
            form = PostNewForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
               post = form.save()
               post.tag_set.add(*post.extract_tag_list())
               return redirect(post)
        else:
            form = PostNewForm(instance=post)
        
        context = {'form':form}
        return render(request, 'instargram/post_form.html', context)
    else:
        return redirect(post)
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'instargram/post_confirm_delete.html'
    success_url = reverse_lazy('instargram:post_list')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('/')