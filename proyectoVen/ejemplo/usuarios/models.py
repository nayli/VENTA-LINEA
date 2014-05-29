from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	ci=models.IntegerField(null=False,verbose_name="Ci")
	nombre = models.CharField(max_length=90,null=False,verbose_name="Nombre Completo")
	apellidos=models.CharField(max_length=90,null=False,verbose_name="Apellidos")
	email=models.EmailField(null=False,verbose_name="Email")
	direccion=models.CharField(max_length=90,null=False,verbose_name="Direccion")
	ciudad=models.CharField(max_length=90,null=False,verbose_name="Ciudad")
	telefono = models.IntegerField(null=True,verbose_name="telefono/cel")
	user = models.ForeignKey(User, null=True, blank=True, unique=True)