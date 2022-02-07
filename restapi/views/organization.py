from django.db.models import Prefetch

from rest_framework import generics, permissions

from apps.customers.models import organization as models_organization
from apps.customers.models import department as models_department
from restapi.serializers import organization as restapi_organization


class OrganizationListAPIView(generics.ListAPIView):
    swagger_schema = None
    serializer_class = restapi_organization.OrganizationSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = models_organization.Organization.objects.prefetch_related(
            Prefetch('departments', queryset=models_department.Department.objects.select_related(
                'parent').prefetch_related('children').filter(parent__isnull=True))).all()
        return queryset
