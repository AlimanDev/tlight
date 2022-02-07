from rest_framework import generics, permissions

from apps.customers.models import client as models_client
from restapi.serializers import client as restapi_client


class ClientListAPIView(generics.ListAPIView):
    serializer_class = restapi_client.ClientSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = models_client.Client.objects.prefetch_related(
            'emails', 'phone_more', 'social_accounts').filter(
            is_staff=False, is_superuser=False
        )
        return queryset
