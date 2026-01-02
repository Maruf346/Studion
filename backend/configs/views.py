from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.permissions import IsAdminUser # type: ignore
from .models import EmailConfig, SMSConfig, SSLCommerzConfig
from .serializers import *


class SingletonConfigAPIView(APIView):
    permission_classes = [IsAdminUser]
    model = None
    serializer_class = None

    def get_object(self):
        return self.model.get_solo()

    def get(self, request):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):
        obj = self.get_object()
        serializer = self.serializer_class(
            obj, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class EmailConfigAPIView(SingletonConfigAPIView):
    model = EmailConfig
    serializer_class = EmailConfigSerializer


class SMSConfigAPIView(SingletonConfigAPIView):
    model = SMSConfig
    serializer_class = SMSConfigSerializer


class SSLCommerzConfigAPIView(SingletonConfigAPIView):
    model = SSLCommerzConfig
    serializer_class = SSLCommerzConfigSerializer

