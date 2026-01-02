from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from user.permissions import IsAdminOrReadOnly

class CompanyInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class NavMenuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = NavMenu.objects.all()
    serializer_class = NavMenuSerializer


class HeroMottoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = HeroMotto.objects.all()
    serializer_class = HeroMottoSerializer


class HeroSliderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = HeroSlider.objects.all().order_by("priority")
    serializer_class = HeroSliderSerializer

class OfferBannerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = OfferBanner.objects.all()
    serializer_class = OfferBannerSerializer

class CustomerReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class SuggestionMessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]  # need to recheck later
    queryset = SuggestionMessage.objects.all()
    serializer_class = SuggestionMessageSerializer

class DynamicScriptsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = DynamicScripts.objects.all()
    serializer_class = DynamicScriptsSerializer


# New ViewSets
class AdditionalInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer
    
class RefundPolicyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = RefundPolicy.objects.all()
    serializer_class = RefundPolicySerializer
    
class ShippingPolicyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ShippingPolicy.objects.all()
    serializer_class = ShippingPolicySerializer
    
class PrivacyPolicyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    
class ShopLocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ShopLocation.objects.all()
    serializer_class = ShopLocationSerializer

class TermsAndConditionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = TermsAndConditions.objects.all()
    serializer_class = TermsAndConditionsSerializer

class PhotoGalleryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    
    
class PartialPaymentDescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PartialPaymentDescription.objects.all()
    serializer_class = PartialPaymentDescriptionSerializer


class FAQViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    

class AnnouncementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    search_fields = ['title', 'content']
    filterset_fields = ['is_active']
    

class PopUpBannerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PopUpBanner.objects.all()
    serializer_class = PopUpBannerSerializer
    filterset_fields = ['is_active']