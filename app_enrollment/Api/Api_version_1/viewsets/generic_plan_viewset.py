from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#=====================================
# App Imports
#=====================================
from app_enrollment.Api.Api_version_1.serializers.generic_plan_serializer import GenericPlanSerializer
from app_enrollment.models import GenericPlan


class GenericPlanViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = GenericPlan.objects.all()
    serializer_class = GenericPlanSerializer