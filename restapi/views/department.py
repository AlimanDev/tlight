from django.db.models import Prefetch

from rest_framework import generics, permissions

from apps.customers.models import department as models_department
from restapi.serializers import department as restapi_department


class DepartmentListAPIView(generics.ListAPIView):
    serializer_class = restapi_department.DepartmentListSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = models_department.Department.objects.select_related(
            'parent', 'legal_person').prefetch_related(
            Prefetch('children',
                     queryset=models_department.Department.objects.select_related(
                         'parent').prefetch_related('children').all())).filter(parent__isnull=True)
        return queryset
