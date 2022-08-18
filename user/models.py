from django.db import models
from django.db.models import CASCADE

from location.models import Location


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

	def __str__(self):
		return self.username
