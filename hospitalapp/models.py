from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length = 50, default="harry")
    address = models.CharField(max_length = 100, default="hogwarts")
    phno = models.CharField(max_length = 50, default="987654321")
    field = models.CharField(max_length = 50, default="flying")
    email = models.EmailField(max_length = 255, default="abc@gmail.com")
    username = models.CharField(max_length = 50, default="")
    password = models.CharField(max_length = 50, default="")

class patient(models.Model):
    name = models.CharField(max_length = 50, default="harry")
    address = models.CharField(max_length = 100, default="hogwarts")
    phno = models.CharField(max_length = 50, default="987654321")
    email = models.EmailField(max_length = 255, default="abc@gmail.com")
    