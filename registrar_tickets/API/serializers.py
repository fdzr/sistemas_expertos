# -*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-


from ..models import Ticket

from rest_framework import serializers


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'titulo', 'descripcion', 'estado', 'creado']


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['titulo', 'descripcion', 'estado']
