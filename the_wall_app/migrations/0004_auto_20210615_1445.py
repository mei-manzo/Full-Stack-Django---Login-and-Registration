# Generated by Django 2.2 on 2021-06-15 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall_app', '0003_auto_20210615_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='poster',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='poster',
        ),
    ]