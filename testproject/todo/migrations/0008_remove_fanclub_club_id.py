# Generated by Django 3.1.7 on 2021-03-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_user_following_clubs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fanclub',
            name='club_id',
        ),
    ]
