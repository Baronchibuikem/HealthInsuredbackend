from rest_framework import serializers
from app_enrollment.models import PlanRegistration, CustomUser
import datetime


class PlanRegistrationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlanRegistration
        fields = ('id', 'password', 'first_name', 'last_name', 'username', 'email', 'state', 'gender',
                  'plan_name', 'unique_id', 'expired', 'state', 'plan_name', 'json', 'date_registered')
        read_only_fields = ('id', 'unique_id', 'expired', 'date_registered')

# class PlanRegSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlanRegistration
#         fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source="group.name")

    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = 'group', 'groups', 'user_permissions',
