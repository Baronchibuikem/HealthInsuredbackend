from rest_framework import serializers
from app_enrollment.models import Dependent


class DependentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dependent
        fields = "__all__"
