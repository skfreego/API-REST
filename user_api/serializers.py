from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
                  'first_name',
                  'last_name',
                  'mobile_number',
                  'email',
                  'dob',
                  'password'
    )


class ProfileGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
                  'id',
                  'first_name',
                  'last_name',
                  'mobile_number',
                  'email',
                  'dob',
                  'password')


class ProfileViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
                  'id',
                  'first_name',
                  'last_name',
                  'mobile_number',
                  'email',
                  'dob',
                  'password')