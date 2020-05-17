from rest_framework import serializers
from app_claims.models import Claim, Batch


class ClaimsSerializer(serializers.ModelSerializer):
    """
        This is used to serializer all the fields we wish to pass information,
        This serializer servers for Uploading claims, vetting claims, marking 
        claims as complete and also editing claim,

        Uploading Claims --> Fields that are required to be field can be displayed
        in the frontend while others that are not have a null and blank set to True

        Claim_vetting --> Fields that are required to vet a claim can be displayed in 
        the Frontend and a PATCH request can be made to update that field

        Claim_complete --> This involves making a PATCH request to update the completed
        boolean field to True
    """
    # date_created = serializers.DateTimeField(format="%Y-%m-%d")
    batch_id = serializers.CharField(
        source='claim_batch.id',
        read_only=True
    )

    # claim_batch = serializers.CharField(source="claim_batch.name")
    class Meta:
        model = Claim
        fields = ('id', 'first_name', 'last_name', 'unique_id', 'date_of_birth', 'date_created', 'phone_number',
                  'guardian_name', 'gender', 'address', 'patient_complaints',
                  'amount_claimed', 'claim_batch', 'batch_id', 'examination_findings',
                  'management', 'family_planning', 'out_patient_consultation',
                  'drugs_given', 'caregiver_surname', 'caregiver_firstname',
                  'caregiver_date_uploaded', 'caregiver_health_facility', 'caregiver_phone_number',
                  'completed', 'vetted', 'amount_claimed', 'amount_to_pay', 'amount_denied', 'reason')
        read_only_fields = ('id',)
