from django.db import models
from django_ckeditor_5.fields import CKEditor5Field # type: ignore


class ServiceCategory(models.Model):
    icon = models.ImageField(upload_to="service/category/icons/")
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.title


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services"
    )
    name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to="service/images/",
        null=True,
        blank=True
    )
    description = CKEditor5Field(null=True, blank=True, config_name='default')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
