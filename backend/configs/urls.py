from django.urls import path
from .views import (
    EmailConfigAPIView,
    SMSConfigAPIView,
    SSLCommerzConfigAPIView,
)

urlpatterns = [
    path("email/", EmailConfigAPIView.as_view(), name="email-config"),
    path("sms/", SMSConfigAPIView.as_view(), name="sms-config"),
    path("sslcommerz/", SSLCommerzConfigAPIView.as_view(), name="sslcommerz-config"),
]
