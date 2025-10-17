from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Contacts, Projects
from .serializers import ContactsMessageSerializers, ProjectSerializer

@api_view(['POST'])
def contact_message(request):
    serializer = ContactsMessageSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Message submitted successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def contactsList(request):
    contact = Contacts.objects.all().order_by('-created_at')
    serializer = ContactsMessageSerializers(contact, many=True, context = {'request' : request})
    return Response(serializer.data)

@api_view(['GET'])
def projectList(request):
    projects = Projects.objects.all().order_by('-created_at')
    serializer = ProjectSerializer(projects, many=True, context={'request' : request})
    return Response(serializer.data)