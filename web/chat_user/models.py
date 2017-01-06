from django.db import models

# Create your models here.
class User(models.Model):
	f_name=models.CharField(max_length=200)
	l_name=models.CharField(max_length=200)
	
class Chat(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	message = models.CharField(max_length=200)

	def __unicode__(self):
		return self.message