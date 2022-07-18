from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    
    context = {'form':form}
    return render(request, 'accounts/signup_form.html', context)