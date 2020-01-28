from django.db import models

# Create your models here.


class VisitorMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(default='<No message>')
