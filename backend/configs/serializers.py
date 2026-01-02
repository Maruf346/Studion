from rest_framework import serializers # type: ignore
from .models import EmailConfig, SMSConfig, SSLCommerzConfig



class EmailConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfig
        fields = "__all__"
        read_only_fields = ("id",)


class SMSConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSConfig
        fields = "__all__"
        read_only_fields = ("id",)


class SSLCommerzConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSLCommerzConfig
        fields = "__all__"
        read_only_fields = ("id",)
