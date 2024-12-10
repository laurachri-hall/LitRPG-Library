# Generated by Django 4.2.16 on 2024-12-09 10:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("review", "0006_review_updated_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_reviews", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
