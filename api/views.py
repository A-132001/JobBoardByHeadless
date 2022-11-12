from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from .serializers import JobSerialzer,UserSerialzer,UploadSerialzer
from .models import Job,UploadFiles
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
@api_view(["GET","POST"])
def jobs_api(request):
    # Get
    if request.method == "GET":
        jobs = Job.objects.all()
        serialzer = JobSerialzer(jobs,many=True)
        return Response(serialzer.data)
    elif request.method == "POST":
        serialzer = JobSerialzer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def job_details (request,id):
    try:
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialzer = JobSerialzer(job)
        return Response(serialzer.data)
    elif request.method == "PUT":
        serialzer = JobSerialzer(job,data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data,status=status.HTTP_400_BAD_REQUEST)     
    elif request.method == "DELETE":
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Api With ViewSets
class viewset_Job(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerialzer
    # authentication_classes = [TokenAuthentication]



# Auth Api 
class userViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny,]
    def create(self,request,*args,**kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token,created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {'token':token.key},status=status.HTTP_201_CREATED
        )
    def list(self,request,*args,**kwargs):
        response = {'message':"You cann't create list to users"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,*args,**kwargs):
        response = {'message':"You cann't update user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        response = {'message':"You cann't delete user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)

class UploadViewset(viewsets.ModelViewSet):
    queryset = UploadFiles.objects.all()
    serializer_class = UploadSerialzer
