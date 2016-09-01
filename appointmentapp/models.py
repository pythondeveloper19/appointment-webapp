from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Appointments(models.Model):
    datetime=models.CharField(max_length=1000)
    description=models.CharField(max_length=900)

    def __unicode__(self):
        return self.description
