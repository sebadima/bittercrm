from django.db import models

class Poll(models.Model):
    campo1 = models.CharField(max_length=200)
    campo2 = models.CharField(max_length=200)
    campo3 = models.CharField(max_length=200)
    campo4 = models.CharField(max_length=200)
    campo5 = models.CharField(max_length=200)
    campo6 = models.CharField(max_length=200)
    campo7 = models.CharField(max_length=200)
    campo8 = models.DateTimeField('data ultima consegna')

