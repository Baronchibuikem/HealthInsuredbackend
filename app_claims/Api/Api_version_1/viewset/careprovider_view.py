from rest_framework import viewsets, filters
from app_claims.models import CareProvider
from app_claims.Api.Api_version_1.serializers.careprovider_serializer import CareProviderSerializer
from rest_framework import permissions


class CareProviderView(viewsets.ModelViewSet):
    '''
    For rendering the serialized fields of the Batch model
    '''
    search_fields = ['name', 'lga']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CareProviderSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    name = "careprovider_list"

    def get_queryset(self):
        """
        Optionally filter returned care providers against an 'lga' query parameter in the URL
        """
        queryset = CareProvider.objects.all()
        lga = self.request.query_params.get('lga', None)
        if lga is not None and lga != '':
            queryset = queryset.filter(lga=lga)
        return queryset
