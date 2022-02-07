from rest_framework import serializers
from apps.customers.models import department
from restapi.serializers.organization import OrganizationSerializer


class DepartmentListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='uid')
    organization = OrganizationSerializer()

    class Meta:
        model = department.Department
        exclude = (
            'parent',
        )

    def get_fields(self):
        fields = super(DepartmentListSerializer, self).get_fields()
        fields['children'] = DepartmentListSerializer(many=True, required=False)
        return fields