from rest_framework import serializers # type: ignore
from .models import *

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = "__all__"

class SupportSerializer(serializers.ModelSerializer):
      class Meta:
            model = support
            fields = "__all__"