from django.db import models

# Create your models here.


class Image(models.Model):
    CATEGORIES = [
        ('Birds (photography)', 'Birds'),
        ('Waterfowls (photography)', 'Waterfowls'),
        ('Madison, WI (photography)', 'Madison, WI'),
        ('Other (photography)', 'Other'),
        ('Paintings (photography)', 'Paintings')
    ]

    full_image_file = models.ImageField(upload_to='images/full')
    thumbnail = models.ImageField(upload_to='images/thumbnails')
    caption = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, null=True, blank=True)
    featured = models.BooleanField(default=False)
    ranking = models.IntegerField(default=0)
