from django.conf.urls import url
from API.views import TicketListAPIView, CreateTicketAPIView

urlpatterns = [
    url(r'create/$', CreateTicketAPIView.as_view(), name='create'),
    url(r'^$', TicketListAPIView.as_view(), name='list'),


]
