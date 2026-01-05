from rest_framework.viewsets import ModelViewSet
from .models import ServiceCategory, Service
from .serializers import *
from user.permissions import IsAdminOrReadOnly


class ServiceCategoryViewSet(ModelViewSet):
    queryset = ServiceCategory.objects.prefetch_related("services")
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.select_related("category")
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

