from rest_framework import serializers
from app_enrollment.models import GenericPlan

class GenericPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericPlan
        fields = ('plan_name', 'price',)
