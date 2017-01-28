from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Transaction(models.Model):

      date= models.DateTimeField()

      pid= models.CharField(max_length=20)
      userid = models.CharField(max_length=20)
        issuedby= models.CharField(max_length=100)
