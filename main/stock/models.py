from django.db import models
from .choices import *
from ..models import Level
import os

# Create your models here.

class Item(models.Model):
    description = models.CharField(max_length=50)
    level = models.ForeignKey(
        Level, models.SET_NULL, related_name='items', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    reserve_quantity = models.IntegerField(default=0)
    reserve_quantity_max = models.IntegerField(default=5)
    type = models.CharField(max_length=20,choices=ITEM_TYPES)


    def __str__(self):
        return "%s | %s | %s | %d" % (self.description,self.level,self.type,self.quantity)

    @property
    def summary(self):
        return str(self)


class Transaction(models.Model):
    item = models.ForeignKey(
        Item, models.SET_NULL, related_name='transactions', blank=True, null=True)
    tx_quantity = models.IntegerField()
    operation = models.CharField(max_length=6,choices=TX_OPS)
    date = models.DateField()
    #reason = models.CharField(max_lenth=50,blank=True)

    def __str__(self):
        return "%s | %s | %s | %d" % (self.date, self.item,self.operation,self.tx_quantity)

    @property
    def summary(self):
        return str(self)
