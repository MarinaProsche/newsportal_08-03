# Generated by Django 4.1.5 on 2023-02-18 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0010_rename_subscriber_subscriberscathegory_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
