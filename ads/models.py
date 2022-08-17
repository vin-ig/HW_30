from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Location(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lng = models.DecimalField(max_digits=9, decimal_places=6)

	class Meta:
		verbose_name = 'Локация'
		verbose_name_plural = 'Локации'


class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	role = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
	location = models.ForeignKey(Location, on_delete=CASCADE)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Ad(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete=CASCADE)
	price = models.IntegerField()
	description = models.TextField(max_length=1000)
	is_published = models.BooleanField()
	image = models.ImageField(upload_to='images/')
	category = models.ForeignKey(Category, on_delete=CASCADE)

	class Meta:
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'
