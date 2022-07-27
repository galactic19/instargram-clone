from django.contrib import messages
from django.contrib.auth import login as auth_login, get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, logout_then_login,
    PasswordChangeView as Auth_PasswordChangeView,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import SignUpForm, ProfileForm, PasswordChageForm
from .models import User


class UserLogin(LoginView):
    model = User
    template_name = 'accounts/login_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            '''
                로그인 상태 접근 거부 
            '''
            return redirect('/')       
        return super().dispatch(request, *args, **kwargs) 
login = UserLogin.as_view()


def logout(request):
    if request.user.is_authenticated:
        messages.success(request, '로그아웃 되었습니다.')
        return logout_then_login(request)
    else:
        '''
            비로그인자가 접근시 로그인url로 이동
        '''
        return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            sign_user = form.save()
            auth_login(request, sign_user)
            messages.success(request, '회원가입을 완료 하였습니다.')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'accounts/signup_form.html', context)


@login_required
def profile_list(request):
    return render(request, 'accounts/profile_list.html')



@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            messages.success(request, '프로필 정보가 수정 되었습니다.')
            form.save()
    else:
        form = ProfileForm(instance=request.user)
        
    context = {'form': form}
    return render(request, 'accounts/profile_edit_form.html', context)


class PasswordChangeView(LoginRequiredMixin, Auth_PasswordChangeView):
    success_url = reverse_lazy('accounts:profile_list')
    template_name = 'accounts/passrowd_change_form.html'
    form_class = PasswordChageForm
    
    def form_valid(self, form):
        messages.success(self.request, '비밀번호가 변경 되었습니다.')
        return super().form_valid(form)


password_change = PasswordChangeView.as_view()


@login_required
def user_follow(request, username):
    target_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    get_user(request).following_set.add(target_user)
    target_user.follower_set.add(request.user)

    print(get_user(request).follower_set.filter(pk=target_user.pk))
    messages.success(request, '팔로우 했습니다.')
    redirect_url = request.headers.get('HTTP_REFERER', 'root')
    return redirect(redirect_url)


@login_required
def user_unfollow(request, username):
    unfair = get_object_or_404(get_user_model(), username=username) # 구독을 끊기 위한 user 정보
    get_user(request).following_set.remove(unfair) # 내 정보에서 구독되어있는 위 사람의 정보를 제거
    unfair.follower_set.remove(get_user(request)) # 구독되어있는 사람에게서 구독중인 유저의 정보를 삭제
    messages.success(request, f'{unfair.username} 님을 언팔로우 했습니다.')
    redirect_url = request.headers.get('HTTP_REFERER', 'root')
    return redirect(redirect_url)