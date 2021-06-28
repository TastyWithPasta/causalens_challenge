from django.db import models

# Create your models here.
class Kvp(models.Model):
    key = models.CharField(max_length=255) # TODO: Clarify requirements
    value = models.CharField(max_length=255) # TODO: Clarify requirements