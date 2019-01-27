# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ticket

# Register your models here.

admin.site.site_header = 'Panel de administracion Sistemas Expertos'


class TicketAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'estado', 'creado')
    list_filter = ('creado', 'titulo', 'estado')
    search_fields = ('titulo', 'creado', 'estado')


admin.site.register(Ticket, TicketAdmin)
