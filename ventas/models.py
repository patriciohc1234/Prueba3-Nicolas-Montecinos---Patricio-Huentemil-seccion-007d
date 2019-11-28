from django.db import models
from django.db import models
from django.urls import reverse

class Catalogo(models.Model):
    
	title = models.CharField(max_length=200)
	precio = models.TextField(max_length=1000)
	descripcion = models.CharField(max_length=200)
	
	def __str__(self):
		return self.title
