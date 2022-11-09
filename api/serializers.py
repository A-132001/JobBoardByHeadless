from rest_framework import  serializers
from .models import Job,UploadFiles
from django.contrib.auth.models import User

class JobSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'



class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['username','email','password']

        extra_kwargs = {'password':{'write_only':True,'required':True},'email':{'required':True}}

class UploadSerialzer(serializers.ModelSerializer):
    class Meta:
        model =  UploadFiles
        fields = ['file']