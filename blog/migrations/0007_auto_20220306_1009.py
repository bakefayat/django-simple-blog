# Generated by Django 3.2.6 on 2022-03-06 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created'], 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='body', max_length=1000, verbose_name='متن نظر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='bakefayat98@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='نظر'),
            preserve_default=False,
        ),
    ]