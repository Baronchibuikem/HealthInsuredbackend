from rest_framework import viewsets
from app_claims.models import Batch
from app_claims.Api.Api_version_1.serializers.batch_upload_serializer import BatchUploadSerializer
from rest_framework.response import Response
from rest_framework import permissions

class BatchUpload(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Batch model
    '''
    queryset = Batch.objects.all()
    serializer_class = BatchUploadSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    name = "batch_payment_instance"
