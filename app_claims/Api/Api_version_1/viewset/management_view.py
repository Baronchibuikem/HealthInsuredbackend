from rest_framework import viewsets
from app_claims.models import Management
from app_claims.Api.Api_version_1.serializers.management_serializer import ManagementSerializer
from rest_framework import permissions


class ManagementView(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Management model
    '''
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)