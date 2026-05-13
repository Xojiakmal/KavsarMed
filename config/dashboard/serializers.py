from rest_framework import serializers
from .models import *


class AddClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class AddServicesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesType
        fields = ['name', 'value']

class AddServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['service_name', 'client']

class GetClientsSerializer(serializers.ModelSerializer):
    fish = serializers.SerializerMethodField()

    class Meta:
        model = Clients
        fields = ['id', 'fish', 'mfy', 'phone_number', 'age', 'gender']

    def get_fish(self, obj):
        return obj.first_name + ' ' + obj.last_name

class ReportServicesListSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = ServicesType
        fields = ['name', 'total_amount', 'count']

    def get_total_amount(self, obj):
        queryset = Services.objects.filter(service_name_id=obj.id).aggregate(models.Sum('service_name__value'))

        return queryset["service_name__value__sum"]

    def get_count(self, obj):
        queryset = Services.objects.filter(service_name_id=obj.id).count()

        return queryset