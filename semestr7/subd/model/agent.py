# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import DateTimeField, GenericIPAddressField


class Agent(models.Model):

    class Meta:
        app_label = "subd"
        verbose_name = "Агент"
        verbose_name_plural = "Агенты"

    fio = models.CharField("ФИО", max_length=200)
    filial = models.ForeignKey("Filial", verbose_name="филиал")

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"{0.fio}".format(self)
