# Generated by Django 5.1.1 on 2024-10-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pixel", "0003_rename_name_photo_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="description",
            field=models.TextField(default="photo", unique=True),
        ),
    ]