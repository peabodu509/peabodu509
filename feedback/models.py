from django.db import models
from django.utils import timezone	
# Create your models here.
class Feedback(models.Model):
	good = models.TextField()
	bad = models.TextField()
	proposal = models.TextField()
	created_date = models.DateTimeField(default = timezone.now )
	number = models.IntegerField(default = 0) 

	def __str__(self):
		return str(self.id)