from rest_framework import serializers
from app_claims.models import Payment, Claim
from django.utils import timezone

class CustomManager(object):
    """
    Here we are defining our own custom object since the fields we will be using for the Payment logic
    ain't all perculiar to the Payment model.

    The fields we will be using are passed as parameter once the CustomManager object is instansiated
    """
    def __init__(self, 
    id, 
    reason_approved_or_denied, 
    total_approved, 
    batch, batch_id, 
    is_approved, 
    date_created,
    vetted_claims,
    total_claims):
        self.id = id
        self.reason_approved_or_denied = reason_approved_or_denied
        self.total_approved = total_approved
        self.batch = batch
        self.batch_id = batch_id
        self.is_approved = is_approved
        self.date_created = date_created
        self.vetted_claims = vetted_claims
        self.total_claims = total_claims

class AcceptPaymentSerializer(serializers.Serializer):
    """
     This serializer class is used to update the following fields 'reason', 'amount_to_pay', 'amount_denied" 
     in Payment model
     """
    id = serializers.ReadOnlyField()
    batch = serializers.CharField(source='batch.name', read_only=True)
    batch_id = serializers.CharField(source='batch.batch_id', read_only=True)
    reason_approved_or_denied = serializers.CharField()
    total_approved = serializers.IntegerField(read_only=True)
    is_approved = serializers.ReadOnlyField(default=False)
    vetted_claims = serializers.ReadOnlyField()
    total_claims = serializers.ReadOnlyField()
    date_created = serializers.DateField(format="%Y-%m-%d", read_only=True)

    def create(self, validated_data):
        unapproved_payments = Payment.objects.filter(pk=validated_data['id'], is_approved=False).first()
        claims = Claim.objects.filter(claim_batch__id=unapproved_payments.batch.id)

        unapproved_payments.reason_approved_or_denied = validated_data['reason_approved_or_denied']
        unapproved_payments.is_approved = True
        unapproved_payments.date_approved = timezone.now()

        unapproved_payments.save()
        return unapproved_payments

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.reason_approved_or_denied = validated_data.get('reason_approved_or_denied', instance.reason_approved_or_denied)
        instance.save()
        return instance



class RejectPaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    reason_approved_or_denied = serializers.CharField()


    def create(self, validated_data):
        unapproved_payments = Payment.objects.filter(pk=validated_data['id'], is_approved=False).first()
        claims = Claim.objects.filter(claim_batch__id=unapproved_payments.batch.id)

        unapproved_payments.reason_approved_or_denied = validated_data['reason_approved_or_denied']
        unapproved_payments.is_approved = False
        unapproved_payments.date_approved = timezone.now()

        unapproved_payments.save()
        return unapproved_payments


