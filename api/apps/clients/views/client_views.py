from rest_framework.generics import ListAPIView

from apps.clients.models import Client
from apps.clients.serializers import ClientSerializer


class ClientList(ListAPIView):

    queryset = Client.objects.filter(status=True)
    serializer_class = ClientSerializer
