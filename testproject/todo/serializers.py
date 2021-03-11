from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FanclubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanclub
        fields = '__all__'


class BasicFanclubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanclub
        fields = ('name', 'des', 'image')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_detail
        fields = '__all__'


class BasicUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_detail
        fields = ('user_id', 'user_name', 'user_profile_image')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
