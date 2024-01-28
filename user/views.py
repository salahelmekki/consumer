from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import UserCustomerSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# api to create use
class CreateCustomer(APIView):
    def post(self, request):
        data = self.request.data
        serializer = UserCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# api for logging
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
