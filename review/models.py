from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from star_ratings.models import Rating

# Define STATUS choices
STATUS = ((0, "Draft"), (1, "Published"))


class Book(models.Model):
    book_cover = CloudinaryField('image')
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    series_name = models.CharField(max_length=200, blank=True)
    series_volume = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.book_title} | written by {self.book_author}"


class Review(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE, related_name="review")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews")
    book_cover = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="book_cover_reviews",
        null=True, blank=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="liked_reviews", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.user}"

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    review = models.ForeignKey(
            Review, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True  # Allow empty input
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.content} | by {self.user}"
    def total_likes(self):
        return self.likes.count()
