from django.db import models

# Create your models here.

class Blogs(models.Model): #class name must be caps
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
