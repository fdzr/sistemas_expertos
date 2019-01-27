# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Ticket(models.Model):
    ABIERTO = 'abierto'
    PENDIENTE = 'pendiente'
    EN_PROCESO = 'en_proceso'
    RESUELTO = 'resuelto'
    CERRADO = 'cerrado'

    ESTADOS_CHOICES = ((ABIERTO, 'Abierto'),
                       (PENDIENTE, 'Pendiente'),
                       (EN_PROCESO, 'En Proceso'),
                       (RESUELTO, 'Resuelto'),
                       (CERRADO, 'Cerrado'))

    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=15, choices=ESTADOS_CHOICES)
    creado = models.DateTimeField(default=timezone.now)  # ().strftime('%b %d %Y')

    def __str__(self):
        return self.titulo
