# Generated by Django 4.1.1 on 2022-09-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_profile_photo_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
