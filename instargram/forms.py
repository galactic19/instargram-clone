from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post, Tag

class PostNewForm(forms.ModelForm):
    # caption = SummernoteTextFormField()
    class Meta:
        model = Post
        fields = ['photo', 'caption', 'location']
        widgets = {
            'caption': SummernoteWidget(),
        }