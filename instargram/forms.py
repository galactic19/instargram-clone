from django import forms
from django.forms import Textarea
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post, Tag, Comment

class PostNewForm(forms.ModelForm):
    # caption = SummernoteTextFormField()
    class Meta:
        model = Post
        fields = ['photo', 'caption', 'location', 'is_used']
        widgets = {
            'caption': SummernoteWidget(),
        }


class CommentNewForm(forms.ModelForm):
    content = forms.Textarea()
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'rows':3, 
                                       'class': 'rounded-0 border-end-0 border-start-0 p-0 m-0',
                                       'placeholder': '댓글을 입력하세요',
                                       }),
        }
        labels = {
            'content': ''
        }
