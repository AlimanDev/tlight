from django.urls import path
from restapi.views import client, organization, department

app_name = 'restapi'

urlpatterns = [
    path('departments/', department.DepartmentListAPIView.as_view()),
    path('clients/', client.ClientListAPIView.as_view()),
    path('organizations/', organization.OrganizationListAPIView.as_view())
]