from django.db import models
from django.contrib.auth.models import User
from main.models import Pocket

class Order(models.Model):
    domen = models.URLField(max_length=100)
    contacts = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    reason = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    client = models.ForeignKey(User)
    is_processed = models.BooleanField(default=True)
    pocket = models.ForeignKey(Pocket, null=True)

    def __unicode__(self):
        return self.client.username