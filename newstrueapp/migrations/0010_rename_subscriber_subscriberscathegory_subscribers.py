# Generated by Django 4.1.5 on 2023-02-15 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0009_rename_subscribers_subscriberscathegory_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriberscathegory',
            old_name='subscriber',
            new_name='subscribers',
        ),
    ]
