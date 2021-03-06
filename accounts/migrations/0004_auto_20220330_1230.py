# Generated by Django 3.2.6 on 2022-03-30 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0003_remove_logs_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='logs',
            name='log',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin.logentry', verbose_name='رویداد'),
        ),
    ]
