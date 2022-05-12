from distutils.command.upload import upload
import email
from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from pendulum import datetime
import phonenumbers
from sqlalchemy import false, null



class account(models.Model):
    SEX = (
        ('male','male'),
        ('female','female'),
        ('binary','binary'),
    )
    fName = models.CharField(max_length=250)
    lName = models.CharField(max_length=250)
    TimeJoin = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to ='uploads/% Y/% m/% d/',
                            blank=True,null=True)
    Bio = models.TextField(null=True)
    dateBrith = models.DateTimeField(null=True)
    userName = models.CharField(max_length=60, unique=True,
                                null=false)
    email = models.EmailField(unique=True)
    websit = models.CharField(max_length=250, null=True)
    phonenumber = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, choices=SEX, default='male')