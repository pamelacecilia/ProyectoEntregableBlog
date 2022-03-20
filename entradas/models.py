from django.db import models

# Create your models here.
class Crearpost (models.Model):
    titulo= models.CharField(max_length=40)
    subtitulo:models.CharField(max_length=40)
    cuerpo:models.CharField(max_length=200)
    tags:models.CharField(max_length=30)

    
class Contactame(models.Model):
    nombre:models.CharField(max_length=30)
    email:models.EmailField()
    mensaje:models.CharField(max_length=200)
    
    
class Usuarios(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email:models.EmailField()
    

class Buscarpost(models.Model):
    tags=models.CharField(max_length=20)