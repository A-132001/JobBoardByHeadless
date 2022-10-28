from django.db import models

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