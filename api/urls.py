from .views import jobs_api,job_details
from django.urls import path

app_name = 'api'

urlpatterns  =[
    path("jobs/",jobs_api,name='jobs'),
    path("jobs/<int:id>/",job_details,name='job_details'),
]