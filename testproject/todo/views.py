from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializisedData = UserSerializer(
            data, context={'request': request}, many=True)
        return Response(serializisedData.data)

    elif request.method == 'POST':
        serializisedData = UserSerializer(data=request.data)
        if serializisedData.is_valid():
            serializisedData.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializisedData.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, username, userpassword):
    try:
        user = User.objects.get(user_name=username, user_password=userpassword)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_data = User_detail.objects.get(user_id=user.id)
        serializisedData = UserDetailsSerializer(user_data)
        return Response(serializisedData.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(
            user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    