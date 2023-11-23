from django.db import models
from django.contrib.auth.models import User

'''
    MODELO 'Cliente':
    - user: Relación 1 a 1 con modelo 'User'
    - descripcion: str
    - link: str
    - avatar: file
    - metodo str: el usuario se mostrará por su nombre
'''
class Cliente(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='nombre o apodo')
    descripcion = models.CharField(max_length=255, null=True, verbose_name='Cuentanos más de ti.')
    link        = models.URLField(max_length=100, null=True, verbose_name='Instagram, Facebook, Tik Tok, etc.')
    avatar      = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name='Deja que los demas te conozcan.')

    def __str__(self):
        return self.user.username

'''
    MODELO 'Cliente':
    - user: Relación 1 a 1 con modelo 'User'
    - descripcion: str
    - link: str
    - avatar: file
    - metodo str: el instructor se mostrará por su nombre, y se identificará como tal.
''' 


class Instructor(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='nombre o apodo')
    descripcion = models.CharField(max_length=255, null=True, verbose_name='Cuentanos más de ti.')
    link        = models.URLField(max_length=100, null=True, verbose_name='Instagram, Facebook, Tik Tok, etc.')
    avatar      = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name='Deja que los demas te conozcan.')

    def __str__(self):
        return self.user.username
