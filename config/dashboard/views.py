from django.db.models import Count, Sum
from rest_framework.response import Response

from .serializers import *
from rest_framework import generics

# Create your views here.

class AddClientViewSet(generics.CreateAPIView):
    serializer_class = AddClientSerializer

class AddServicesViewSet(generics.CreateAPIView):
    serializer_class = AddServicesSerializer

class GetClientsViewSet(generics.ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = GetClientsSerializer

class AddServicesTypeViewSet(generics.ListCreateAPIView):
    serializer_class = AddServicesTypeSerializer
    queryset = ServicesType.objects.all()

class ReportServicesViewSet(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        services = ServicesType.objects.all()
        services_serializer = ReportServicesListSerializer(services, many=True)

        today_clients = Services.objects.values('client').annotate(total=Count('client')).count()
        male_clients = Clients.objects.filter(gender='Erkak').count()
        female_clients = Clients.objects.filter(gender='Ayol').count()
        total_amount = Services.objects.aggregate(total=Sum('service_name__value'))['total']

        page = self.paginate_queryset(services)
        if page is not None:
            services_serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "Services": services_serializer.data,
                "Statistics": {
                    'today_clients': today_clients,
                    'male_clients': male_clients,
                    'female_clients': female_clients,
                    'total_amount': total_amount
                }
            })


        return Response({
            "Services": services_serializer.data,
            "Statistics": {
                'today_clients': today_clients,
                'male_clients': male_clients,
                'female_clients': female_clients,
                'total_amount': total_amount
            }
        })
