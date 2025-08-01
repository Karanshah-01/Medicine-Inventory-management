from django.urls import path
from .views import index, MedicineListCreate, MedicineDetail

urlpatterns = [
    path('', index, name='home'),  # your frontend entry point

    # Custom API endpoints (not using DRF router)
    path('api/medicines/', MedicineListCreate.as_view(), name='medicine-list-create'),
    path('api/medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
]
