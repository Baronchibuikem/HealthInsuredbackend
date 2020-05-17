from rest_framework import serializers
from app_claims import models
from django.utils import timezone
from .claim_serializer import ClaimsSerializer


class BatchUploadSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    batch_id = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    created_by = serializers.CharField(max_length=50)
    date_created = serializers.ReadOnlyField(default=timezone.now)

    claims = ClaimsSerializer(many=True, read_only=True, required=False)

    def create(self, validated_data):
        new_batch = models.Batch(
            batch_id = validated_data.get('batch_id'),
            name = validated_data.get('name'),
            created_by = validated_data.get('created_by')
        )
        new_batch.save()
        new_pay = models.Payment()
        new_pay.batch = new_batch

        new_pay.save()
        new_batch.save()

        return new_batch
