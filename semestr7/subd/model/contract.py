# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import DateTimeField, GenericIPAddressField


class Contract(models.Model):

    class Meta:
        app_label = "subd"
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"

    class Type:
        AUTO = 'A'
        HOUSE = 'H'
        MEDICINE = 'M'
        CHOICES = (
            (AUTO, 'Автотраспорт от угона'),
            (HOUSE, 'Домашнее имущество'),
            (MEDICINE, 'Добровольное медицинское'),
        )

    type = models.CharField("тип", max_length=1, choices=Type.CHOICES)
    amount = models.DecimalField("Сумма", max_digits=8, decimal_places=2)
    comission = models.DecimalField("Комиссия", max_digits=8, decimal_places=2)
    tariff = models.DecimalField("Тариф %", max_digits=8, decimal_places=2)
    date = models.DateTimeField("Дата")
    filial = models.ForeignKey("Filial", verbose_name="филиал")
    client = models.ForeignKey("Client", verbose_name="клиент")
    agent = models.ForeignKey("Agent", verbose_name="агент")

    def save(self, *args, **kwargs):
        self.comission = round(self.amount / 100 * self.tariff, 2)
        super(Contract, self).save(*args, **kwargs)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"{0.id}".format(self)
