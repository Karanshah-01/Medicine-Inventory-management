from django.urls import path
from .views import index, MedicineListCreate, MedicineDetail

urlpatterns = [
    path('', index, name='home'),  # frontend entry point
    path('api/medicines/', MedicineListCreate.as_view(), name='medicine-list-create'),
    path('api/medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
]
