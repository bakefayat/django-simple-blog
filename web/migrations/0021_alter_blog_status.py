# Generated by Django 3.2.6 on 2021-09-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0020_alter_blog_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[
                    ("d", "پیش نویس"),
                    ("p", "منتشر شده"),
                    ("w", "در انتظار تایید"),
                    ("r", "رد شده"),
                ],
                max_length=1,
                verbose_name="وضعیت",
            ),
        ),
    ]
