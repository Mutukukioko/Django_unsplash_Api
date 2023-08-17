from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    photographer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
