# Generated by Django 4.1.5 on 2023-02-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0017_alter_post_date_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
