from ..models import Ticket
from .serializers import TicketListSerializer, TicketCreateSerializer

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated


class TicketListAPIView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer


class CreateTicketAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    permission_classes = [IsAuthenticated, ]
