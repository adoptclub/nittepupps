from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from django.utils import timezone
from datetime import datetime
import django
from django.conf import settings
from django import forms
# Create your models here.


class User(AbstractUser):
    Username = models.CharField(max_length=100, unique=True, default=django.utils.timezone.now)
    password = models.CharField(max_length=100, default=django.utils.timezone.now)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.Username




class Customer(models.Model):

    username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    email_number = models.CharField(max_length=50, unique=True)
    # conf_password = models.CharField(max_length=20, default="")
    rescue = models.BooleanField(default=False)
    shelter = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=5)
    # is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now)
    # USERNAME_FIELD = 'username'
    # EMIAL_FIELD = 'email_number'
    # REQUIRED_FIELDS = [username,password,first_name,last_name,email_number,conf_password,rescue,age]

    @classmethod
    def create_user(cls, username, first_name, last_name, email_number, shelter, age, is_active,date_joined
    ):
        print('hielo ')
        book = cls(username=username,first_name=first_name,last_name=last_name,
        email_number=email_number,shelter=shelter,age=age,date_joined=date_joined)

        return book


    def __str__(self):
        return self.username

class RescueComplaint(models.Model):
    date_complaint = models.DateTimeField(default=django.utils.timezone.now)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    street_address1 = models.CharField(max_length=3000)
    street_address2 = models.CharField(max_length=3000)
    city = models.CharField(max_length=300)
    region = models.CharField(max_length=300)
    postalcode = models.CharField(max_length=500)
    country = models.CharField(max_length=300)
    date_incident = models.DateField()
    incident_location = models.CharField(max_length=500)
    details = models.CharField(max_length=5000)


    @classmethod
    def create(cls, date_complaint,username,email,street_address1,street_address2,city,region,postalcode,
    country,date_incident,incident_location,details
    ):
        book = cls(username=username,email=email,street_address1=street_address1,street_address2=street_address2
        ,city=city,region=region,postalcode=postalcode,country=country,date_incident=date_incident,
        incident_location=incident_location,details=details)
        # do something with the book
        return book

class Feedback_Note(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=5000)
    @classmethod
    
    def create(cls, name=name, email=email, comment=comment):
        book = cls(name=name, email=email, comment=comment)
        return book
    def __str__(self):
        return self.email
    