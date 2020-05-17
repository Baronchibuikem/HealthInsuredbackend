from rest_framework import viewsets
from app_claims.models import OutPatientConsultation
from app_claims.Api.Api_version_1.serializers.outpatient_consultation_serializer import OutPatientConsultationSerializer
from rest_framework import permissions


class OutPatientConsultationView(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Management model
    '''
    queryset = OutPatientConsultation.objects.all()
    serializer_class = OutPatientConsultationSerializer
    # permission_classes = (permissions.IsAuthenticated,)