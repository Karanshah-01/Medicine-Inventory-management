"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from medicine.views import MedicineViewSet
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# router = DefaultRouter()
# router.register(r'medicines', MedicineViewSet)

# schema_view = get_schema_view(
#     openapi.Info(title="Medicine API", default_version='v1'),
#     public=True,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
# ]

from django.urls import path, include
from medicine.views import MedicineListCreate, MedicineDetail
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="Medicines Custom API", default_version='v2'),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/medicines/', MedicineListCreate.as_view(), name='medicine-list-create'),
    path('api/medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include('medicine.urls')),
]
