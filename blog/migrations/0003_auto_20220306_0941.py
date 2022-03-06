# Generated by Django 3.2.6 on 2022-03-06 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('display', models.BooleanField(default=False, verbose_name='نمایش')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='blog.comment', verbose_name='نظر'),
        ),
    ]
