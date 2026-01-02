from rest_framework.routers import DefaultRouter # type: ignore
from django.urls import path, include
from drf_spectacular.views import ( # type: ignore
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = DefaultRouter()

"""API URL Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Papyrus API",
        default_version='v1',
        description="API documentation for Papyrus",
         terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="maruf.bshs@gmail.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
"""
urlpatterns = [
    # path('', include(router.urls)),   
    path("configs/", include("configs.urls")), 
    
    # Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
]


