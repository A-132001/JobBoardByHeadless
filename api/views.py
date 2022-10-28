from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from .serializers import JobSerialzer
from .models import Job
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
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
