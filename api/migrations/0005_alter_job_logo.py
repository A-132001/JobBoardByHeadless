# Generated by Django 4.1.2 on 2022-11-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_job_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='JobsLogos'),
        ),
    ]
