from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100, blank=True)
    roleta = models.BooleanField(default=False)
    dados = models.BooleanField(default=False)
    football = models.BooleanField(default=False)

    def __str__(self):
        return self.cpf
    
    class Meta:
        verbose_name = 'Clients'
        verbose_name_plural = 'Clients'