from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hostal(models.Model):
	nom =  models.TextField(max_length=100)
	direccio = models.TextField(max_length=100, null=True)
	telefon = models.CharField(max_length=12, null=True)
	def __unicode__(self):
		return self.nom	

class Client(models.Model):
	nom = models.ForeignKey(User)
	direccio = models.TextField(max_length=100)
	telefon = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nom.username

class Habitacio(models.Model):
	hostal = models.ForeignKey(Hostal)
	numero_habitacio = models.CharField(max_length=3)
	preu_nit = models.CharField(max_length=6)
	def __unicode__(self):
		return self.hostal.nom+" - "+self.numero_habitacio+" - "+self.preu_nit
			
	
class Reserva(models.Model):
	habitacio =  models.ForeignKey(Habitacio)
	client =  models.ForeignKey(Client)
	data_ent = models.DateTimeField()
	data_sort = models.DateTimeField()
	confirmada = models.BooleanField(default=True)
	qualificacio = models.IntegerField(default=0)
	comentari_qualificacio = models.TextField(max_length=150, blank=True)
	def __unicode__(self):
		return self.client.nom.username+" - "+self.habitacio.numero_habitacio+" - "+self.habitacio.hostal.nom
