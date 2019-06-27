from django.db import models
    # Create your models here.
photo = models.ImageField(upload_to="gallery")
class User(models.Model):
    # Fields
    email = models.EmailField(max_length=255, help_text='Enter Email')
    password = models.CharField(max_length=30, help_text='Enter Password')
