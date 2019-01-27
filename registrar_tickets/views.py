# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from .models import Ticket

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super(IndexView, self).get_context_data(*args, **kwargs)
        context_data['ticket'] = Ticket.objects.all()
        return context_data


class AddTicketView(TemplateView):
    template_name = 'add_ticket.html'
