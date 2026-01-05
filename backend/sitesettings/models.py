from django.db import models

# Create your models here.
class Footer(models.Model):
      phone = models.CharField(max_length=20, null=True, blank=True)
      email = models.EmailField(null=True, blank=True)
      timing = models.CharField(max_length=100, null=True, blank=True)
      address = models.CharField(max_length=255, null=True, blank=True)
      facebook = models.URLField(null=True, blank=True)
      twitter = models.URLField(null=True, blank=True)
      instagram = models.URLField(null=True, blank=True)
      linkedin = models.URLField(null=True, blank=True)
      youtube = models.URLField(null=True, blank=True)
      about = models.TextField(null=True, blank=True)

      def __str__(self):
            return "Footer Information"

class support(models.Model):
      points = models.CharField(max_length=255, null=True, blank=True)
      url = models.URLField(null=True, blank=True)

      def __str__(self):
            return self.points