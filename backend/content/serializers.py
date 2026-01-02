from rest_framework import serializers # type: ignore
from .models import *


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"
        read_only_fields = ['id']


class NavMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavMenu
        fields = "__all__"
        read_only_fields = ['id']


class HeroMottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroMotto
        fields = "__all__"
        read_only_fields = ['id']


class HeroSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlider
        fields = "__all__"
        read_only_fields = ['id']
        
class OfferBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferBanner
        fields = "__all__"
        read_only_fields = ['id']

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = "__all__"
        read_only_fields = ['id']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
        read_only_fields = ['id']

class SuggestionMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionMessage
        fields = "__all__"
        read_only_fields = ['id']

class DynamicScriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicScripts
        fields = "__all__"
        read_only_fields = ['id']
        

# New Serializers
class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = "__all__"
        read_only_fields = ['id']
        

class RefundPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefundPolicy
        fields = "__all__"
        read_only_fields = ['id']
        
class ShippingPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingPolicy
        fields = "__all__"
        read_only_fields = ['id']
        
class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = "__all__"
        read_only_fields = ['id']
        
class ShopLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopLocation
        fields = "__all__"
        read_only_fields = ['id']
        
class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = "__all__"
        read_only_fields = ['id']
        
class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = "__all__"
        read_only_fields = ['id']
        
        
class PartialPaymentDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartialPaymentDescription
        fields = "__all__"
        read_only_fields = ['id']
        

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
        read_only_fields = ['id']
        

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
        read_only_fields = ['id']
        
        
class PopUpBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUpBanner
        fields = "__all__"
        read_only_fields = ['id']