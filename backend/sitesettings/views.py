from rest_framework import viewsets # type: ignore
from .models import *
from .serializers import *
from user.permissions import IsAdminOrReadOnly

# Create your views here.
class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [IsAdminOrReadOnly]

class SupportViewSet(viewsets.ModelViewSet):
    queryset = support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [IsAdminOrReadOnly]


