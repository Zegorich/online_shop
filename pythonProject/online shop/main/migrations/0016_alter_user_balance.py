# Generated by Django 5.0.3 on 2024-05-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_flag_registration_code_user_registration_code_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Баланс'),
        ),
    ]