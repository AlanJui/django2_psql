from django.db import models
from django.urls import reverse

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.')
)

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)
    email = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    # headshot = models.ImageField(upload_to='author_headshots', blank=True)
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={ 'pk': self.pk })

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()