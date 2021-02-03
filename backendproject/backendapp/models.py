from django.db import models

# Create your models here.

class User(models.Model):
	firstName = models.CharField(max_length=80)
	lastName = models.CharField(max_length=80)
	mail = models.CharField(max_length=120)
	password = models.CharField(max_length=120)

def __str__(self):
	return self