from rest_framework import viewsets, generics
from app_claims.models import Claim, Batch
from app_claims.Api.Api_version_1.serializers.claim_serializer import ClaimsSerializer
from rest_framework import permissions
from rest_framework.response import Response


class ClaimView(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Batch model
    '''
    queryset = Claim.objects.all()
    serializer_class = ClaimsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)

