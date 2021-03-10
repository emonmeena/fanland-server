from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import *
from .serializers import *
import json


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        username = request.data['username']
        userpassword = request.data['password']
        try:
            user = User.objects.get(
                user_name=username, user_password=userpassword)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializisedData = UserSerializer(user)
        return Response(serializisedData.data)

    elif request.method == 'POST':
        serializised_user = UserSerializer(data=request.data)
        if serializised_user.is_valid():
            serializised_user.save()
            return Response(serializised_user.data['id'])
        return Response(serializised_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', ])
def user_details(request):
    if request.method == 'GET':
        print(request.data['user_id'])
        try:
            user_detail_data = User_detail.objects.get(
                user_id=request.data['user_id'])
        except User_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializisedData = UserDetailsSerializer(
            user_detail_data, context={'request': request})
        return Response(serializisedData.data)

    elif request.method == 'POST':
        serialised_user_detail = UserDetailsSerializer(data=request.data)
        if serialised_user_detail.is_valid():
            serialised_user_detail.save()
            return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        print(request.data['user_id'])
        try:
            user_detail_data = User_detail.objects.get(
                user_id=request.data['user_id'])
        except User_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailsSerializer(
            user_detail_data, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch_user(request, username):
    try:
        user = User.objects.get(user_name=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_data = User_detail.objects.get(user_id=user.id)
        serializisedData = UserDetailsSerializer(user_data)
        return Response(serializisedData.data)


@api_view(['GET', 'POST'])
def fanclub_list(request):
    if request.method == 'GET':
        data = Fanclub.objects.all()
        serializisedData = FanclubSerializer(
            data, context={'request': request}, many=True)
        return Response(serializisedData.data)

    elif request.method == 'POST':
        serializisedData = FanclubSerializer(data=request.data)
        if serializisedData.is_valid():
            serializisedData.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializisedData.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fanclub_details(request, club_id):
    try:
        fanclub = Fanclub.objects.get(id=club_id)
    except Fanclub.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializisedData = FanclubSerializer(fanclub)
        return Response(serializisedData.data)

    elif request.method == 'PUT':
        serializer = FanclubSerializer(
            fanclub, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fanclub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def chat_list(request, chatroom_id):
    if request.method == 'GET':
        data = Chat.objects.filter(chatroom_id=chatroom_id)
        serializisedData = ChatSerializer(
            data, context={'request': request}, many=True)
        return Response(serializisedData.data)

    elif request.method == 'POST':
        serializisedData = ChatSerializer(data=request.data)
        if serializisedData.is_valid():
            serializisedData.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializisedData.errors, status=status.HTTP_400_BAD_REQUEST)
