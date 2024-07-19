# Generated by Django 4.2.11 on 2024-07-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_profile_delete_appuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
