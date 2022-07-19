from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from .models import User
from .forms import SignUpForm


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
        form = SignUpForm(request.POST)
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