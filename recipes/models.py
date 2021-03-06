from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=100)


    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author.name}"

