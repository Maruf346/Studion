from rest_framework import viewsets, status # type: ignore
from rest_framework.decorators import action # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser # type: ignore
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from django.core.mail import send_mail
from django.utils import timezone
from configs.models import EmailConfig
from django.conf import settings
from .models import PasswordResetRequest
# Extra imports for Google Auth
from google.oauth2 import id_token # type: ignore
from google.auth.transport import requests # type: ignore
# Extra imports for OpenAPI
from drf_spectacular.utils import ( # type: ignore
    extend_schema,
    extend_schema_view,
)
from drf_spectacular.utils import OpenApiResponse # type: ignore

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    search_fields = ["email", "first_name", "last_name"]
    filterset_fields = ["is_staff", "is_active", "gender"]
    ordering_fields = ["date_joined", "email", "first_name", "last_name"]
    ordering = ["-date_joined"]
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UserProfileSerializer   # show full profile information
        if self.action in ["register"]:
            return UserRegisterSerializer
        if self.action in ["update_profile"]:
            return UserProfileSerializer
        if self.action in ["google_auth"]:
            return GoogleAuthSerializer
        return UserProfileSerializer


    def get_permissions(self):
        if self.action in ["register", "login", "google_auth"]:
            return [AllowAny()]
        elif self.action in ["profile", "update_profile"]:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserRegisterSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=UserLoginSerializer,
        responses={200: "Successful login", 401: "Invalid credentials"},
    )
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, email=email, password=password)
        if not user:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserRegisterSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "is_staff": user.is_staff,
            }
        )

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logged out"})
        except Exception:
            return Response(
                {"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def profile(self, request):
        # /users/profile/ 
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
    )
    @extend_schema(
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
    )
    @action(detail=False, methods=["put", "patch"], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        # /users/update_profile/
        partial = request.method.lower() == "patch"
        serializer = UserProfileSerializer(request.user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserProfileSerializer(user).data)
    
    # Google Authentication
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def google_auth(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )
        except ValueError:
            return Response(
                {"detail": "Invalid Google token"},
                status=status.HTTP_400_BAD_REQUEST
            )

        email = idinfo.get("email")
        first_name = idinfo.get("given_name", "")
        last_name = idinfo.get("family_name", "")
        picture = idinfo.get("picture")

        if not email:
            return Response(
                {"detail": "Email not available from Google"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "is_active": True,
            },
        )

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserProfileSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "is_new_user": created,
        })


"""
    @extend_schema(auto_schema=None)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
"""



User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def send_reset_otp(request):
    email = request.data.get('email')
    if not email:
        return Response({"detail": "Email is required."}, status=400)

    # Generic success message for privacy
    GENERIC_MSG = {"detail": "If the account exists, an OTP has been sent to the email."}

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(GENERIC_MSG, status=200)

    # previous pending request?
    pr = PasswordResetRequest.objects.filter(user=user, verified=False).order_by("-created_at").first()

    if pr and pr.resend_count >= PasswordResetRequest.MAX_RESEND:
        return Response({"detail": "Too many OTP sends. Try later."}, status=429)

    if not pr:
        pr = PasswordResetRequest(user=user)
    else:
        pr.resend_count += 1

    otp = PasswordResetRequest.generate_otp()
    pr.set_otp(otp)
    pr.save()
    
    email_config = EmailConfig.get_solo()

    send_mail(
        subject="Your Password Reset OTP",
        message=(
        "Dear Valued Customer,\n\n"
        "We received a request to reset the password for your Zenshop Builder account.\n\n"
        f"Your One-Time Password (OTP) is: {otp}\n"
        "This OTP is valid for the next 5 minutes. Please do not share this code with anyone.\n\n"
        "If you did not request a password reset, please ignore this email or contact our support team immediately.\n\n"
        "Kind regards,\n"
        "Zenshop Builder Support Team\n"
        "Email: info@ZenshopBuilder.com\n"
        "Website: https://www.ZenshopBuilder.com"
    ),
        from_email=email_config.default_from_email,
        recipient_list=[user.email],
        fail_silently=False,
        auth_user=email_config.email_host_user,
        auth_password=email_config.email_host_password,
    )

    return Response(GENERIC_MSG, status=200)



@api_view(['POST'])
@permission_classes([AllowAny])
def verify_reset_otp(request):
    email = request.data.get('email')
    otp = request.data.get('otp')

    if not email or not otp:
        return Response({"detail": "Email and OTP are required."}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"detail": "Invalid OTP."}, status=400)

    pr = PasswordResetRequest.objects.filter(user=user, verified=False).order_by('-created_at').first()
    if not pr:
        return Response({"detail": "No reset request found."}, status=404)

    if pr.verify_attempts >= PasswordResetRequest.MAX_VERIFY:
        return Response({"detail": "Too many attempts."}, status=429)

    if timezone.now() > pr.otp_expires_at:
        return Response({"detail": "OTP expired."}, status=400)

    if not pr.check_otp(otp):
        pr.verify_attempts += 1
        pr.save()
        return Response({"detail": "Invalid OTP."}, status=400)

    pr.verified = True
    pr.save()

    return Response({"detail": "OTP verified."}, status=200)



@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    email = request.data.get('email')
    new_pass = request.data.get('password')

    if not email or not new_pass:
        return Response({"detail": "Email and password are required."}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"detail": "Invalid request."}, status=400)

    pr = PasswordResetRequest.objects.filter(user=user, verified=True).order_by('-created_at').first()
    if not pr:
        return Response({"detail": "OTP not verified."}, status=400)

    user.set_password(new_pass)
    user.save()

    # clean request
    pr.delete()

    return Response({"detail": "Password reset successful."}, status=200)
