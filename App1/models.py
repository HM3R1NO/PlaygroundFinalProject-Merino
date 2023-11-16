from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self): #De esta forma el elemento del modelo Post tendra el nombre del título ingresado
        return self.title
