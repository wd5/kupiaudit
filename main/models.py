from django.db import models

class Pocket(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="pockets_image")
    mini_description = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name
