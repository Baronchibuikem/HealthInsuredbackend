"""
module for Staff viewset from rest_framework API view
API endpoint that allows Staff to be viewed or edited
refrences: (https://bit.ly/2QVPtX9), (https://bit.ly/2SZ4D0x)
"""

#=====================================
# Package imports
#=====================================
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#=====================================
# App Imports
#=====================================
from app_enrollment.Api.Api_version_1.serializers.staff_serializer import StaffSerializer
from app_enrollment.models import Staff


class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
