# Generated by Django 4.1.5 on 2023-02-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0007_alter_post_head_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriberscathegory',
            old_name='subscriber',
            new_name='subscribers',
        ),
    ]
