from rest_framework import viewsets, filters, generics, serializers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from app_enrollment.models import CustomUser, PlanRegistration
from app_enrollment.Api.Api_version_1.serializers.plan_registration_serializer import PlanRegistrationSerializer, CustomUserSerializer
from rest_framework import permissions, filters


class QueryAllUsersView(viewsets.ModelViewSet):
    '''
    This view is responsible for querying all the registered users in the database
    and filtering them out by their unique ID's.
    '''
    search_fields = ['unique_id', ]
    filter_backends = (filters.SearchFilter,)
    queryset = PlanRegistration.objects.all()
    serializer_class = PlanRegistrationSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CustomUserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
