# Generated by Django 4.1.2 on 2022-10-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('type', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('log', models.ImageField(blank=True, null=True, upload_to='')),
                ('salary', models.IntegerField()),
                ('vacancy', models.IntegerField()),
            ],
        ),
    ]