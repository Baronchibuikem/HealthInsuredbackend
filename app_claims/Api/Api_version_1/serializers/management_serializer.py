from rest_framework import serializers
from app_claims.models import Management


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ('name',)