from django import forms
from .models import Post, Tag

class PostNewForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['photo', 'caption', 'tag_set']