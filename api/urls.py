from .views import jobs_api,job_details,viewset_Job,userViewset,UploadViewset
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register("jobs",viewset_Job)
router.register("users",userViewset)
router.register("upload",UploadViewset)
app_name = 'api'

urlpatterns  =[
    path("jobs/",jobs_api,name='jobs'),
    path("jobs/<int:id>/",job_details,name='job_details'),

    #url for viewsets
    path("viewsets/",include(router.urls)),
    path("api-auth-token/",obtain_auth_token)
    
    
]