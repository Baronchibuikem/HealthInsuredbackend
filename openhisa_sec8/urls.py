"""openhisa_sec8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from openhisa_sec8 import settings
from rest_framework_swagger.views import get_swagger_view

#==================================
#DJANGO ADMIN custom
#==================================
admin.site.site_header = "OpenHisa"
admin.site.site_title = "OpenHisa Staff Portal"
admin.site.index_title = "Welcome to OpenHisa Staff Portal"

schema_view = get_swagger_view(title='OpenHISA Api Documentation')

urlpatterns = [
    # This will take you to the different endpoints in app_enrollment
    path('api/v1/enrollment/', include('app_enrollment.Api.Api_version_1.urls')),

    # This will take you to the different endpoints in app_claim
    path('api/v1/claims-processing/', include('app_claims.Api.Api_version_1.urls')),

    # This will take you to the admin interface
    path('admin/', admin.site.urls),

    # This will show you all the available endpoint in this project
    path('', schema_view),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)