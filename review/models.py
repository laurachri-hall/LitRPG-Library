from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Define STATUS choices 
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Book(models.Model):
    book_cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    series_name = models.CharField(max_length=200, blank=True)
    series_volume = models.PositiveIntegerField(null=True, blank=True)
     

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
   
    def __str__(self):
        return f'Review for {self.book.title}'