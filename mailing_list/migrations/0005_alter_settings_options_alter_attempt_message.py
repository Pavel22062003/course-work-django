# Generated by Django 4.2.1 on 2023-06-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0004_alter_settings_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'permissions': [('can_deactivate_settings', 'Can deactivate settings')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AlterField(
            model_name='attempt',
            name='message',
            field=models.CharField(verbose_name='сообщение'),
        ),
    ]
