from rest_framework import serializers
from app_claims.models import CareProvider


class CareProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareProvider
        fields = ( 'id', 'name', 'lga',)

