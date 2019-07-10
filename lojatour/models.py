from django.db import models

# Create your models here.
class Login(models.Model):
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    estado = models.CharField(max_length=20)
    #aparezca en el admin
    class Meta:
        verbose_name= "Login"
        verbose_name_plural = "Logins"
        #lo que va a retornar
    def __str__(self):
        return self.usuario

