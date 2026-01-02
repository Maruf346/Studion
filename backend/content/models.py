from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field # type: ignore


# Create your models here.
class CompanyInfo(models.Model):
      ComLogo = models.ImageField(upload_to='navbar/com_logo')
      ComName = models.CharField(max_length=100)
      ComEmail = models.EmailField(blank=True, null=True)
      ComPhone = models.CharField(max_length=20, blank=True, null=True)
      ComAbout = models.TextField(blank=True, null=True)
      ComAddress = models.CharField(max_length=255, blank=True, null=True)
      ComGMapHTML = models.TextField(null=True, blank=True)
      ComBusinessHours = models.CharField(max_length=100, null=True, blank=True)

      def __str__(self):
            return self.ComName

class NavMenu(models.Model):
      MenuName = models.CharField(max_length=100, null=True, blank=True)
      MenuLogo = models.ImageField(upload_to='navbar/menu_logo', null=True, blank=True)
      url = models.URLField(null=True, blank=True)

      def __str__(self):
            return self.MenuName

class HeroMotto(models.Model):
      motto_title = models.CharField(max_length=100, null=True, blank=True)
      moto_subtitle = models.CharField(max_length=200, null=True, blank=True)
      motto_desc = models.CharField(max_length=255, null=True, blank=True)

      def __str__(self):
            return self.motto_title

class HeroSlider(models.Model):
      motto = models.ForeignKey(HeroMotto, on_delete=models.CASCADE)
      image = models.ImageField(upload_to="Hero/")
      priority = models.PositiveIntegerField(default=0)

      class Meta:
          ordering = ["priority"]

      def __str__(self):
          return f"Slider {self.pk} - Priority {self.priority}"

class OfferBanner(models.Model):
      image = models.ImageField(upload_to='OfferBanner/', null=True, blank=True)

      def __str__(self):
            return f"Offer Banner {self.pk}"


class CustomerReview(models.Model):
      name = models.CharField(max_length=100)
      image = models.ImageField(upload_to='CustomerReview/', null=True, blank=True)
      rating = models.PositiveIntegerField()
      comment = models.TextField()

      def __str__(self):
            return self.name

class ContactUs(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      subject = models.CharField(max_length=200)
      message = models.TextField()
      location = models.CharField(max_length=255, null=True, blank=True)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"Message from {self.name} - {self.subject}"

class SuggestionMessage(models.Model):
      text = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.text

class DynamicScripts(models.Model):
      script_name = models.CharField(max_length=100)
      script_content = models.TextField()

      def __str__(self):
            return self.script_name


# New Models
class AdditionalInfo(models.Model):
      info = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Additional Info {self.pk}"
      

class RefundPolicy(models.Model):
      policy = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Refund Policy {self.pk}"

class ShippingPolicy(models.Model):
      policy = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Shipping Policy {self.pk}"

class PrivacyPolicy(models.Model):
      policy = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Privacy Policy {self.pk}"
      
class ShopLocation(models.Model):
      location = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Shop Location {self.pk}"
      
class TermsAndConditions(models.Model):
      terms = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Terms and Conditions {self.pk}"
      
class PhotoGallery(models.Model):
      title = models.CharField(max_length=100)
      image = models.ImageField(upload_to='PhotoGallery/')

      def __str__(self):
            return self.title
      
      
class PartialPaymentDescription(models.Model):
      description = CKEditor5Field(null=True, blank=True, config_name='default')

      def __str__(self):
            return f"Partial Payment Description {self.pk}"
      

class FAQ(models.Model):
      question = models.CharField(max_length=255)
      answer = CKEditor5Field(null=True, blank=True, config_name='default')
      
      class Meta:
          verbose_name = "FAQ"
          verbose_name_plural = "FAQs"

      def __str__(self):
            return self.question
      
      
class Announcement(models.Model):
      title = models.CharField(max_length=200)
      content = CKEditor5Field(null=True, blank=True, config_name='default')
      is_active = models.BooleanField(default=True)

      def __str__(self):
            return self.title
      

class PopUpBanner(models.Model):
      title = models.CharField(max_length=200)
      image = models.ImageField(upload_to='PopUpBanner/')
      content = CKEditor5Field(null=True, blank=True, config_name='default')
      is_active = models.BooleanField(default=True)

      def __str__(self):
            return self.title