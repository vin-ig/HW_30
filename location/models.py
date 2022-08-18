from django.db import models


class Location(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lng = models.DecimalField(max_digits=9, decimal_places=6)

	class Meta:
		verbose_name = 'Локация'
		verbose_name_plural = 'Локации'

	def __str__(self):
		return self.name
