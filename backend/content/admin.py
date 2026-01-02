from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HeroSlider)
admin.site.register(HeroMotto)
admin.site.register(NavMenu)
admin.site.register(CompanyInfo)
admin.site.register(OfferBanner)
admin.site.register(CustomerReview)
admin.site.register(SuggestionMessage)
admin.site.register(ContactUs)
admin.site.register(DynamicScripts)
admin.site.register(AdditionalInfo)
admin.site.register(RefundPolicy)
admin.site.register(ShippingPolicy)
admin.site.register(ShopLocation)
admin.site.register(PhotoGallery)
admin.site.register(TermsAndConditions)
admin.site.register(PartialPaymentDescription)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'pk')
    search_fields = ('question',)
    
@admin.register(PopUpBanner)
class PopUpBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'pk')
    list_filter = ('is_active',)
    search_fields = ('title',)
    
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'pk')
    list_filter = ('is_active',)
    search_fields = ('title',)