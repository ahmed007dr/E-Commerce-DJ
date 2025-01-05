"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar  

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView #JWT VIDEO 43

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# تعريف schema_view باستخدام drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Swagger API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('accounts/',include("accounts.urls")), # singup
    path('accounts/', include('django.contrib.auth.urls')), # video 42 log in & out #https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication#setting_up_your_authentication_views

    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('__debug__/', include(debug_toolbar.urls)),  
    path('',include("settings.urls")),
    path('orders/',include("orders.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #JWT VIDEO 43
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #JWT VIDEO 43

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


