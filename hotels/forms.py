from django import forms
from . models import Reviews


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Reviews
        fields = ['rating', 'body']




