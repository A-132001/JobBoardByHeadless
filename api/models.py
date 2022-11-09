from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Job(models.Model):
    title = models.CharField( max_length=50)
    email = models.EmailField(max_length=50)
    company_name = models.CharField(max_length = 50)
    created_at = models.DateField()
    type = models.IntegerField()
    location = models.CharField(max_length=50)
    log = models.ImageField(blank=True, null=True)
    salary = models.IntegerField()
    vacancy = models.IntegerField()
    def __str__(self):
        return self.title

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



class UploadFiles(models.Model):
    file = models.FileField(upload_to = "UploadedFiles")