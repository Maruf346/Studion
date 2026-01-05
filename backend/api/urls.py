from rest_framework.routers import DefaultRouter # type: ignore
from django.urls import path, include
from drf_spectacular.views import ( # type: ignore
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from content.views import *
from service.views import *
from sitesettings.views import *

router = DefaultRouter()


# Content Section
router.register(r'company-info', CompanyInfoViewSet)
router.register(r'nav-menu', NavMenuViewSet)
router.register(r'hero-motto', HeroMottoViewSet)
router.register(r'hero-slider', HeroSliderViewSet)
router.register(r'offer-banner', OfferBannerViewSet)
router.register(r'customer-review', CustomerReviewViewSet)
router.register(r'contact-us', ContactUsViewSet)
router.register(r'suggestion-message', SuggestionMessageViewSet)
router.register(r'dynamic-scripts', DynamicScriptsViewSet)
    # newly added routers
router.register(r'photo-gallery', PhotoGalleryViewSet)
router.register(r'policy/refund', RefundPolicyViewSet)
router.register(r'policy/shipping', ShippingPolicyViewSet)
router.register(r'policy/privacy', PrivacyPolicyViewSet)
router.register(r'shop-location', ShopLocationViewSet)
router.register(r'additional-info', AdditionalInfoViewSet)
router.register(r'terms-and-conditions', TermsAndConditionsViewSet)
router.register(r'partial-payment-description', PartialPaymentDescriptionViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'announcement', AnnouncementViewSet)
router.register(r'pop-up-banner', PopUpBannerViewSet)

# Service URLs
router.register(r"service-categories", ServiceCategoryViewSet, basename="service-categories")
router.register(r"services", ServiceViewSet, basename="services")

# Site Settings Section
router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'support', SupportViewSet, basename='support')


urlpatterns = [
    path('', include(router.urls)),   
    path("configs/", include("configs.urls")), 
    
    # Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
]


