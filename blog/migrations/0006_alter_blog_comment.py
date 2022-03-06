# Generated by Django 3.2.6 on 2022-03-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='blog.comment', verbose_name='نظرات'),
        ),
    ]