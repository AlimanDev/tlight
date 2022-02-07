from rest_framework import serializers
from apps.customers.models import organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = organization.Organization
        fields = '__all__'
