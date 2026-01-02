from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    # urls.py
    path("password/send-otp/", send_reset_otp),
    path("password/verify-otp/", verify_reset_otp),
    path("password/reset/", reset_password),

    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]