# from django.db import models

# # Create your models here.

# from django.db import models
# import uuid

# class Photo(models.Model):
#     image = models.ImageField(null=False, blank=False)
#     description = models.TextField(max_length=100)

#     def __str__(self):
#         return self.description

# models.py
from django.db import models
import os

def upload_to(instance, filename):
    # Use the fixed folder name based on the instance's upload_folder attribute
    return os.path.join(instance.upload_folder, filename)

class Photo(models.Model):
    image = models.ImageField(upload_to=upload_to, null=False, blank=False)
    description = models.TextField(max_length=100)
    upload_folder = models.CharField(max_length=100, blank=True, default='all/')  # Set by the view to one of the fixed folders

    def __str__(self):
        return self.description
