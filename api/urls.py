from .views import jobs_api,job_details,viewset_Job
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("jobs",viewset_Job)
app_name = 'api'

urlpatterns  =[
    path("jobs/",jobs_api,name='jobs'),
    path("jobs/<int:id>/",job_details,name='job_details'),

    #url for viewsets
    path("viewsets/",include(router.urls))
]