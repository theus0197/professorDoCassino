from django.contrib import admin
from . import models

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email', 'dados', 'football_studio', 'football_dice', 'roleta_evo', 'roleta_playtech')

admin.site.register(models.Clients, ClientsAdmin)