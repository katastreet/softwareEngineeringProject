from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

'''
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # like doc string which returns
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()   # code modified after test
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now
'''


class OfficeData(models.Model):
    '''default productId '''
    productName = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    # model details#
    modelNo = models.CharField(max_length=20, null=True, blank=True)
    modelDate = models.DateField('model date', null=True, blank=True)

    # leasable #
    leasable = models.BooleanField(default=False)
    canBeBought = models.BooleanField(default=False)

    # date details#
    boughtdate = models.DateField('boughtdate')
    warrantyTimeInMonth = models.IntegerField(default=0)

    # rate details#
    boughtprice = models.FloatField(default=0)
    depreciationRate = models.FloatField(default=0)

    # state evaluation #
    previousEvaluationDate = models.DateField('previously evaluated on', blank=True, null=True)
    toBeEvaluatedEveryMonth = models.IntegerField(default=0)
    '''stateCondition ='''

    PRODUCT_TYPE = (
        ('O', 'General Office'),
        ('M', 'Machinary'),
        ('L', 'Agricultural'),
    )
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default='O')

    def __str__(self):
        return self.productName


class WarrantyAgents(models.Model):
    productName = models.ForeignKey(OfficeData, on_delete=models.CASCADE)

    # waranty models #
    warantyAgentName = models.CharField(max_length=200)
    warantyAgentLocation = models.CharField(max_length=200)
    WarantyAgentPhoneNumber = models.CharField(max_length=25)


class PublicUserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productName = models.CharField(max_length=200)
    modelNo = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.productName
