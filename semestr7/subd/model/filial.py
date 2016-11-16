# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import DateTimeField, GenericIPAddressField


class Filial(models.Model):

    class Meta:
        app_label = "subd"
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    address = models.CharField("Адрес", max_length=200)
    phone = models.CharField("Телефон", max_length=200)
    name = models.CharField("Название", max_length=200)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"{0.name}".format(self)
