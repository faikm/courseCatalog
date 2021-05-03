from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length = 200)
	dateOfStart = models.DateField (default = timezone.now, blank = True, null = True)
	dateOfFinish = models.DateField (default = timezone.now, blank = True, null = True)
	numOfLectures = models.IntegerField (blank = True, null = True)


	def __str__(self):
		return self.name
