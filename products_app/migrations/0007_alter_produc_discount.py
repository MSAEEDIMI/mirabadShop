# Generated by Django 5.2.4 on 2025-07-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0006_alter_produc_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produc',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
