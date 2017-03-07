from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Photo(models.Model):
	file = models.ImageField()
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=255, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'photo'
		verbose_name_plural= 'photos'

	def __str__(self):
		return self.name 