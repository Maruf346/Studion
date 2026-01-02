from django.contrib import admin
from .models import EmailConfig, SMSConfig, SSLCommerzConfig


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EmailConfig)
class EmailConfigAdmin(SingletonAdmin):
    list_display = ("email_host", "email_host_user")


@admin.register(SMSConfig)
class SMSConfigAdmin(SingletonAdmin):
    list_display = ("provider_name", "sender_id")


@admin.register(SSLCommerzConfig)
class SSLCommerzConfigAdmin(SingletonAdmin):
    list_display = ("store_id", "sandbox")
