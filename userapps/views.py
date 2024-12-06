from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from . serializers import UserSerializer,ProfileSerailizer,RegistrationSerializer
from . models import Profile
from django.contrib.auth.models import User

# registration
class RegistrationView(APIView):
    def post(self,request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status = status.HTTP_INTERNAL_SERVER_ERROR)
        