from django.db import models
from django.contrib.auth.models import User
from review.models import Book


class ToBeRead(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_be_read_list')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} wants to read {self.book.book_title}"
