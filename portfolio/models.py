from django.db import models

# Create your models here.
class Project(models.Model): #class name must be caps
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/') # need to install pillow
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
#to create migrations
#python manage.py makemigrations
#to apply migrations
#python manage.py migrate
