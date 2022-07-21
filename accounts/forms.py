from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    PasswordChangeForm as Auth_PasswordChangeForm
)
from .models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
    
    username = forms.CharField(max_length=20,
            label='아이디',
            help_text="아이디는 영문+숫자 조합만 가능합니다.")
    
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ['username','email', 'website_url', 'bio']
        fields = ['username', 'email', 'first_name', 'website_url', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('이미 등록된 이메일 주소 입니다.')
        return email



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image','username', 'phone_number', 'gender', 'first_name', 'email', 'bio']
        

class PasswordChageForm(Auth_PasswordChangeForm):
    
    def clean_new_password2(self):
        old_pass = self.cleaned_data.get('old_password')
        new_password2 = super().clean_new_password2()
        
        if old_pass == new_password2:
            raise forms.ValidationError('새로운 비밀번호는 기존 비밀번호와 같을수 없습니다')
        return new_password2