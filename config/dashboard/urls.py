from django.urls import path
from .views import *


urlpatterns = [
    path('clients/Add', AddClientViewSet.as_view()),
    path('clients/List', GetClientsViewSet.as_view()),
    path('services/Type', AddServicesTypeViewSet.as_view()),
    path('services/Report', ReportServicesViewSet.as_view()),
    path('services/Add', AddServicesViewSet.as_view()),
]