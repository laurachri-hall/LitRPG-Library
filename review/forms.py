from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'rating')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'content', 'rating', 'excerpt')