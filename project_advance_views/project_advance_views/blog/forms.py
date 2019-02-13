from django import forms
from .models import Blog_post

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog_post
        fields = ('title', 'content', 'comment_count','picture')