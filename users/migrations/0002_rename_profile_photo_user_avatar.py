# Generated by Django 4.1.1 on 2022-09-24 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="profile_photo",
            new_name="avatar",
        ),
    ]
