# Generated by Django 4.2.9 on 2024-01-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='ForBloggers', max_length=255),
        ),
    ]