from django.contrib import admin
from . import models

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email', 'roleta', 'dados', 'football')

admin.site.register(models.Clients, ClientsAdmin)