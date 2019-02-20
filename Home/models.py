from django.db import models
# Create your models here.


class Snippet(models.Model):
    home_title = models.CharField(max_length=100, default='')
    home_type = models.CharField(max_length=100, default='')
    home_price = models.IntegerField(default='')
    home_photo = models.ImageField(upload_to='home_image', blank=True)
    home_description = models.TextField(max_length=1000, default='')
    # home_owner = models.ForeignKey(add user relationship l8er)
    home_location = models.CharField(max_length=100, default='')
    home_contacts = models.CharField(max_length=100, default='')
