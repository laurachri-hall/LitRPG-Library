from .models import Comment, Review, Book
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.utils.text import slugify


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", "rating")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the rating field as optional
        self.fields["rating"].required = False
        self.fields["rating"].widget.attrs.update({"placeholder": " "})



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("book", "title", "slug", "book_cover", "rating", "content", "excerpt")
        prepopulated_fields = {"slug": ("title",)}
        widgets = {
            "content": SummernoteWidget(),
        }

    def save(self, commit=True):
        # Create a new instance without saving to the database yet
        instance = super().save(commit=False)

        # Automatically generate slug from the title if it's empty
        if not instance.slug:
            instance.slug = slugify(instance.title)

        if commit:
            instance.save()

        return instance


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "book_cover",
            "book_title",
            "book_author",
            "series_name",
            "series_volume",
        )
