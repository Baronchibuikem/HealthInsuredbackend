from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_enrollment.Api.Api_version_1.serializers.dependent_serializer import DependentSerializer
from app_enrollment.models import Dependent


class DependentView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
