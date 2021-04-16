from django.db import models

# Create Models Here
class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")