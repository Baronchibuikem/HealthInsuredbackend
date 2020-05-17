from rest_framework import viewsets
from app_claims.models import FamilyPlanning
from app_claims.Api.Api_version_1.serializers.family_planning_serializer import FamilyPlanningSerializer
from rest_framework import permissions


class FamilyPlanningView(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the FamilyPlanning model
    '''
    queryset = FamilyPlanning.objects.all()
    serializer_class = FamilyPlanningSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)