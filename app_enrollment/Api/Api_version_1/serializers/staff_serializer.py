"""
module for Staff Serializer
model: Staff
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
from app_enrollment.models import Staff


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
