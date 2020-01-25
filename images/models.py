from django.db import models

# Create your models here.


class Image(models.Model):
    full_image_file = None
    thumbnail = None
    caption = ''
    date = ''
    location = ''
    category = ''
    featured = False
