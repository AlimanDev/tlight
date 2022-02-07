from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.urls import path, include, re_path
from restapi import urls

restapi_swagger_scheme_view = get_schema_view(
   openapi.Info(
      title="Test TL API V1",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
        re_path(r'api/v1/', include(urls))
    ])
