# Generated by Django 5.0.3 on 2025-05-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_free',
            field=models.BooleanField(default=False, verbose_name='Это бесплатная публикация?'),
        ),
    ]
