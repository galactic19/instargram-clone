from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입을 완료 하였습니다.')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'accounts/signup_form.html', context)