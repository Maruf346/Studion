from django.db import models
from django.core.exceptions import ValidationError


# Abstract base class for singleton models
class SingletonModel(models.Model):
    # Abstract base class for singleton models.
    # Ensures only one instance exists.

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(
                f"Only one instance of {self.__class__.__name__} is allowed."
            )
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


# Configuration model for Email settings
class EmailConfig(SingletonModel):
    email_backend = models.CharField(
        max_length=255,
        default="django.core.mail.backends.smtp.EmailBackend"
    )
    email_host = models.CharField(max_length=255)
    email_port = models.PositiveIntegerField(default=465)
    email_use_ssl = models.BooleanField(default=True)
    email_use_tls = models.BooleanField(default=False)
    email_host_user = models.EmailField()
    email_host_password = models.CharField(max_length=255)
    default_from_email = models.EmailField()

    def __str__(self):
        return "Email Configuration"


# Configuration model for SMS settings
class SMSConfig(SingletonModel):
    provider_name = models.CharField(max_length=100, default="GreenWeb")
    api_key = models.CharField(max_length=255)
    sender_id = models.CharField(max_length=50)
    api_url = models.URLField(
        default="http://sms.greenheritageit.com/smsapi"
    )

    def __str__(self):
        return "SMS Configuration"


# Configuration model for SSLCommerz payment gateway
class SSLCommerzConfig(SingletonModel):
    store_id = models.CharField(max_length=100)
    store_password = models.CharField(max_length=255)
    sandbox = models.BooleanField(default=True)

    success_url = models.URLField()
    fail_url = models.URLField()
    cancel_url = models.URLField()

    def __str__(self):
        return "SSLCommerz Configuration"
