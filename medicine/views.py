
# # Create your views here.
# from rest_framework import viewsets
# from .models import Medicine
# from .serializers import MedicineSerializer

# class MedicineViewSet(viewsets.ModelViewSet):
#     queryset = Medicine.objects.all()
#     serializer_class = MedicineSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medicine
from .serializers import MedicineSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

def index(request):
    return render(request, "index.html")

# GET /api/medicines/
# POST /api/medicines/
class MedicineListCreate(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=MedicineSerializer)
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET /api/medicines/<id>/
# PUT /api/medicines/<id>/
# PATCH /api/medicines/<id>/
# DELETE /api/medicines/<id>/
class MedicineDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Medicine, pk=pk)

    def get(self, request, pk):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=MedicineSerializer)
    def put(self, request, pk):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MedicineSerializer)
    def patch(self, request, pk):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        medicine = self.get_object(pk)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
