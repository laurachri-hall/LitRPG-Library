# Generated by Django 4.2.16 on 2024-12-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0002_alter_comment_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]
