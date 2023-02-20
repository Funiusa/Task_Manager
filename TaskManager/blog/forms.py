from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "from-control",
            "placeholder": "Your name",
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Live a comment!",
            })
    )

    class Meta:
        model = Comment
        fields = ('author', 'body')
