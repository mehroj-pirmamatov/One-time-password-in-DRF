from django.shortcuts import render
from django.core.cache import cache
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializers,VerifyOtpSerializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer=RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'email ga habar ketdi'})
        return Response(serializer.errors)

class LoginView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializers
    def Post(self,request,*args,**kwargs):
        serializers=VerifyOtpSerializers(data=request.data)
        if serializers.is_valid():
            user=serializers._validated_data['user']

        if not user.is_active:
            user.is_active=True
            user.save()
        cache.delete(f"otp_{user.email}")
        refresh=RefreshToken.for_user(user)

        return Response({
            'message':'Tizimga muvaffaqiyatli kirdingiz',
            'access':str(refresh.access_token),
            'refresh':str(refresh)
        },status=200)
    
        return Response(serializers.errors,status=400)
        