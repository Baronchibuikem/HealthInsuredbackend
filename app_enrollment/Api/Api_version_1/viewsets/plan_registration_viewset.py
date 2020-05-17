from rest_framework import viewsets, filters,generics, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions, filters

from django.utils import timezone
from django.utils.dateparse import parse_date

from datetime import datetime

from dateutil.relativedelta import relativedelta
#=====================================
# App Imports
#=====================================
from app_enrollment.Api.Api_version_1.serializers.plan_registration_serializer import (
    PlanRegistrationSerializer, CustomUserSerializer
    )
from app_enrollment.models import PlanRegistration, CustomUser



class PlanRegistrationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = PlanRegistration.objects.all()
    serializer_class = PlanRegistrationSerializer



class QueryExpiredUsersViews(viewsets.ReadOnlyModelViewSet):
    """
    This view is used to query users whose Policies has expired
    """

    queryset = PlanRegistration.objects.filter(is_expired=True)
    serializer_class = PlanRegistrationSerializer


class QueryUsersExpiringInThreeMonths(viewsets.ReadOnlyModelViewSet):
    """
    This view is used to query users whose Policies will expire three months
    from the current date
    """
    
    three_months = datetime.today() + relativedelta(months=+3)
    # Since django uses aware datetimes we have to convert 3 months to aware datetime
    three_months = timezone.make_aware(three_months, timezone.utc)

    users = PlanRegistration.objects.all()
    serializer_class = PlanRegistrationSerializer
    queryset = users.filter(expired__range=(datetime.today(), three_months))#expired__lte=three_months)

class EnrolleeListView(generics.ListAPIView):
    """
    This view is used to query users who is in the system and whose Policies are active
    by filtering them by their unique_id or email
    """

    # the second part will be done in the frontend when getting the Json value
    # the @ sign breaks the call because only postgress supports full-text search
    # this uses email because emails are unique but names aren't
    search_fields = ['@unique_id','@email']
    serializer_class = PlanRegistrationSerializer
    filter_backends = [filters.SearchFilter,]
    queryset = PlanRegistration.objects.all()

class QueryEnrolleePolicyDate(viewsets.ReadOnlyModelViewSet):
    """
    This view is used to query with dates, all policies expiring within 14 days
    """

    search_fields = ['expired',]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter ]
    serializer_class = PlanRegistrationSerializer
    
    def list(self, request, *args, **kwargs):
        
        date_str = self.request.query_params.get('search')
        date_ = parse_date(date_str)
        
        # we use 15 days because django lookup(range) doesn't include items on the last day
        fifteen_days = date_ + relativedelta(days=+15)
        queryset = PlanRegistration.objects.all().filter(expired__range=(date_, fifteen_days))
    
        serialized_data = self.get_serializer(queryset, many=True)
    
        return Response(serialized_data.data)
    