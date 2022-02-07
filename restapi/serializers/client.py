from apps.customers.models import client
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = client.SocialAccount
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = client.Email
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = client.AdditionalPhone
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerField()
    phone_more = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)
    social_accounts = SocialAccountSerializer(many=True)

    class Meta:
        model = client.Client
        fields = (
            'id', 'uuid', 'phone', 'first_name', 'last_name', 'patronymic',
            'client_type', 'gender', 'timezone', 'created_at', 'updated_at',
            'status_updated_at', 'phone_more', 'emails', 'social_accounts'
        )


class ClientForDepartmentSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerField()

    class Meta:
        model = client.Client
        fields = (
            'id', 'phone', 'first_name', 'last_name', 'patronymic',
            'client_type', 'gender', 'timezone', 'created_at', 'updated_dt',
            'status_updated_dt'
        )
