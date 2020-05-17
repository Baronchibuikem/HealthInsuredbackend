"""
module for Department viewset using rest_framework API view
API endpoint that allows Department to be viewed or edited
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
from app_enrollment.Api.Api_version_1.serializers.department_serializer import DepartmentSerializer

from app_enrollment.models import Department


class DepartmentView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
