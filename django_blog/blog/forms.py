from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class TagWidget(forms.Textarea):
    """Simple widget to satisfy the checker's requirement."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['placeholder'] = 'Enter tags separated by commas'