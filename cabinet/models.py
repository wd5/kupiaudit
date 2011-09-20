          # -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from main.models import Pocket

class Order(models.Model):
    domen = models.URLField(max_length=100, verbose_name="Сайт")
    contacts = models.TextField(blank=True, verbose_name="Контакты")
    keywords = models.TextField(blank=True, verbose_name="Ключевые слова")
    reason = models.TextField(blank=True, verbose_name="Причина обращения")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    client = models.ForeignKey(User)
    is_processed = models.BooleanField(default=True)
    pocket = models.ForeignKey(Pocket, null=True)

    def __unicode__(self):
        return self.client.username