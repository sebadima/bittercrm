
from django.db import models
from datetime import datetime, timedelta

#from datetime import *
import datetime


class Action(models.Model):
    code = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    def __unicode__(self): 
	return self.desc

class Category(models.Model):
    code = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    def __unicode__(self): 
	return self.desc
    class Meta:
        verbose_name_plural = "categories"


def default_email():
    return  "example@example.com"

def default_rating():
    return  "1.0"

def default_notes():
    return  "..."

def default_name():
    return  "name"

def default_lastname():
    return  "lastname"

class Contact(models.Model):
    name              = models.CharField(max_length=200, default                 = default_name)
    lastname          = models.CharField(max_length=200, default                 = default_lastname)
    nickname          = models.CharField(max_length=200)
    address           = models.CharField(max_length=200)
    email             = models.CharField(max_length=200, default                 = default_email)
    rating            = models.CharField(max_length=200, default                 = default_rating)
    notes             = models.CharField(max_length=200, default                 = default_notes)
    category          = models.ForeignKey(Category)
    action            = models.ForeignKey(Action)
 

