from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ValidationSerializer, LawyerSerializer
from .models import Lawyer

# Create your views here.
class Tutorial(APIView):
    def get(self, request):
        payload = {
            "name" : "Nicho",
            "age" : 21
        }
        return Response(
            payload,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        print(request.data)
        return Response(
            "berhasil nih",
            status=status.HTTP_201_CREATED
        )

class ValidationView(APIView):
    def post(self, request):
        serializer = ValidationSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LawyersView(APIView):
    def get(self, request):
        serializer = LawyerSerializer(
            Lawyer.objects.all(),
            many=True
        )

        return Response(serializer.data)
    
    def post(self, request):
        serializer = LawyerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class LawyerDetailView(APIView):
    def get(self, request, id):
        lawyer = get_object_or_404(
            Lawyer.objects.all(),
            id=id
        )

        serializer = LawyerSerializer(lawyer)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def put(self, request, id):
        lawyer = get_object_or_404(
            Lawyer.objects.all(),
            id=id
        )

        serializer = LawyerSerializer(
            lawyer,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        lawyer = get_object_or_404(
            Lawyer.objects.all(),
            id=id
        )

        lawyer.delete()

        return Response(
                status=status.HTTP_204_NO_CONTENT
            )

class GenericLawyersView(ListCreateAPIView):
    serializer_class = LawyerSerializer
    queryset = Lawyer.objects.all()

class GenericLawyerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = LawyerSerializer
    queryset = Lawyer.objects.all()