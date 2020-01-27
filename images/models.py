from django.db import models

# Create your models here.


class Image(models.Model):
    CATEGORIES = [
        ('Birds', 'Birds'),
        ('Waterfowls', 'Waterfowls'),
        ('Madison, WI', 'Madison, WI'),
        ('Other', 'Other'),
        ('Paintings', 'Paintings')
    ]

    full_image_file = models.ImageField(upload_to='images/full')
    thumbnail = models.ImageField(upload_to='images/thumbnails')
    caption = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, null=True)
    featured = models.BooleanField(default=False)
    ranking = models.IntegerField(default=100)
    featured_ranking = models.IntegerField(default=100)
    portrait = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_image_file.url.split('/')[-1]} - {self.category}"
