from rest_framework import serializers
from app_claims.models import OutPatientConsultation


class OutPatientConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPatientConsultation
        fields = ('name',)