from django import forms
from .models import Catalogo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearForm(forms.ModelForm):

	class Meta:
		model = Catalogo

		fields = [
			'title',
			'precio',
			'descripcion',
		]