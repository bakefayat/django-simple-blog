# Generated by Django 3.2.6 on 2021-09-27 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0021_alter_blog_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="is_special",
            field=models.BooleanField(default=False, verbose_name="مقاله ویژه"),
        ),
    ]
