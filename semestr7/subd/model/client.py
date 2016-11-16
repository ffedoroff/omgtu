# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import DateTimeField, GenericIPAddressField


class Client(models.Model):

    class Meta:
        app_label = "subd"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    fio = models.CharField("ФИО", max_length=200)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"{0.fio}".format(self)
