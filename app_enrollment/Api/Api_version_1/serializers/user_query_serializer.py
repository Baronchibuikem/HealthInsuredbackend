from rest_framework import serializers
from app_enrollment.models import CustomUser


class QueryUserSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source="group.name")
    class Meta:
        model = CustomUser
        fields = ("id", "username","group", "state", "gender", "email", "unique_id", 'first_name', 'last_name')