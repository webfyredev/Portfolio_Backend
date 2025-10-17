from rest_framework import serializers
from .models import Contacts, Projects

class ContactsMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"