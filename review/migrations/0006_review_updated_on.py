# Generated by Django 4.2.16 on 2024-12-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
