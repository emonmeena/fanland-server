from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FanclubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanclub
        fields =  '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_detail
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'