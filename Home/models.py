from django.db import models
# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    price = models.IntegerField(default='')
    photo = models.ImageField(upload_to='home_image', blank=True)
    description = models.TextField(max_length=1000, default='')
    # owner = models.ForeignKey(add user relationship l8er)
    location = models.CharField(max_length=100, default='')
    contacts = models.CharField(max_length=100, default='')
