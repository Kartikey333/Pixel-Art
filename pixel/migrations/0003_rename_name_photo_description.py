# Generated by Django 5.1.1 on 2024-10-05 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pixel", "0002_remove_photo_description_photo_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="photo",
            old_name="name",
            new_name="description",
        ),
    ]
