from django.db import models


class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)


class Ad(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	price = models.IntegerField()
	description = models.TextField(max_length=1000)
	address = models.CharField(max_length=100)
	is_published = models.BooleanField()
