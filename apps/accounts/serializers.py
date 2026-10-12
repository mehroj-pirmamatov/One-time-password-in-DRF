from rest_framework import serializers
from .models import CustomUser
import random
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings

class RegisterSerializers(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=CustomUser
        fields=['username','email','password']

    def create(self, validated_data):
        # email=validated_data['email']
        user=CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        otp=str(random.randint(100000, 999999))

        cache.set(f"otp_{user.email}",otp, timeout=300)

        send_mail(
            subject="your otp code",
            message=f"sizning otp codingiz: {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        return user 

class VerifyOtpSerializers(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
    def validate(self,attrs):
        email=attrs['email']
        otp=attrs['otp']
        try:
            user=CustomUser.objects.filter(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("bu email bazada yuq")

        saved_otp=cache.get(f"email: {email}")

        if saved_otp is None:
            raise serializers.ValidationError('otp eskirgan')
        if saved_otp != otp:
            raise serializers.ValidationError("otp xato")

        attrs['user']=user
        return user




