from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):

    username = None   # << DISABLE USERNAME >>

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    email = models.EmailField(unique=True)

    phone_regex = RegexValidator(
        regex=r'^\+8801[3-9]\d{8}$',
        message="Phone number must be in the format +8801XXXXXXXXX (Bangladeshi format)."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=14,
        null=True,
        blank=True,
        help_text="Enter a valid Bangladeshi phone number (e.g., +8801987651234)."
    )

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "email"      # login uses email
    REQUIRED_FIELDS = []          # << minimal change (remove username) >>
    
    objects = UserManager()       # custom manager

    def __str__(self):
        return self.email


User = get_user_model()

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_hash = models.CharField(max_length=255)
    otp_expires_at = models.DateTimeField()
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    verify_attempts = models.PositiveSmallIntegerField(default=0)
    resend_count = models.PositiveSmallIntegerField(default=0)

    MAX_VERIFY = 5
    MAX_RESEND = 3

    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999))

    def set_otp(self, raw_otp, expiry_minutes=5):
        self.otp_hash = make_password(raw_otp)
        self.otp_expires_at = timezone.now() + timezone.timedelta(minutes=expiry_minutes)

    def check_otp(self, raw_otp):
        return check_password(raw_otp, self.otp_hash)
