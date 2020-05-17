"""
module for Department Serializer
model: Department
serializer type: HyperLinkModelSerializer
refrences: (https://bit.ly/2s3kikb), (https://bit.ly/37PG1eR)
"""

#=====================================
# Package imports
#=====================================
from rest_framework import serializers

#=====================================
# App Imports
#=====================================
from app_enrollment.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
