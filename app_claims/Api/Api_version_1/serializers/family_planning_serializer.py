from rest_framework import serializers
from app_claims.models import FamilyPlanning



class FamilyPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPlanning
        fields = ("name",)