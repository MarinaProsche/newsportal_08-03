# Generated by Django 4.1.5 on 2023-02-19 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0013_alter_post_date_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
