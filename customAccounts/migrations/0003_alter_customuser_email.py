# Generated by Django 5.2.4 on 2025-07-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAccounts', '0002_alter_customuser_options_customuser_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='ایمیل'),
        ),
    ]
