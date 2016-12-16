from django.db import models
import os
from django.contrib.auth.models import User
from django.utils import timezone


class Consert(models.Model):
	name = models.CharField(max_length=70)
	theatre = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	time = models.DateTimeField(null = True)
	image_path = models.FilePathField(path='images/', null = True)
	reservation = models.ManyToManyField(User)