# Generated by Django 5.1 on 2024-08-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="head_image",
            field=models.ImageField(blank=True, upload_to="blog/images/%Y/%m/%d/"),
        ),
    ]
