from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250, default='none')
    author = models.CharField(max_length=200, default='none')
    publish_date = models.DateField(default=timezone.now)
    publisher = models.CharField(max_length=200, default='none')
    summary = models.TextField(default='none')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    link = models.URLField(default='https://www.amazon.com')
    image = models.URLField(default='http://g-ec2.images-amazon.com/images/G/01/social/api-share/amazon_logo_500500._V323939215_.png')

    class Meta:
        ordering = ('title',)

"""class Author(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
"""
