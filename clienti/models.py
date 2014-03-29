from django.db import models
from datetime import datetime, timedelta

#from datetime import *
import datetime



class Categorie(models.Model):
    campo1 = models.CharField(max_length=10)
    campo2 = models.CharField(max_length=200)
    def __unicode__(self): 
        return self.campo1


def default_citta():
    return  "citta"

def default_email():
    return  "esempio@esempio.com"

def default_rating():
    return  "1.0"

def default_annotazioni():
    return  "..."

def default_nome():
    return  "nome"

def default_cognome():
    return  "cognome"

class Clienti(models.Model):
    nome              = models.CharField(max_length=200, default                 = default_nome)
    cognome           = models.CharField(max_length=200, default                 = default_cognome)
    ragione_sociale   = models.CharField(max_length=200)
    ragione_sociale   = models.CharField(max_length=200)
    indirizzo         = models.CharField(max_length=200)
    email             = models.CharField(max_length=200, default                 = default_email)
    rating            = models.CharField(max_length=200, default                 = default_rating)
    citta             = models.CharField(max_length=200, default                 = default_citta)
    annotazioni       = models.CharField(max_length=200, default                 = default_annotazioni)
    categoria         = models.ForeignKey(Categorie)
 

