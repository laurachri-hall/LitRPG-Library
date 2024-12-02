from .models import Comment, Review, Book
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'rating')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'book_cover', 'rating', 'content', 'excerpt' )
        widgets = {
            'content': SummernoteWidget(),  
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_cover', 'book_title', 'book_author', 'series_name', 'series_volume')
