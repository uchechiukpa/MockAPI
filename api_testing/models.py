from django.db import models

# Create your models here.
class User_profiles(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    phoneno = models.CharField(max_length=20)


class Projects(models.Model):
       title = models.CharField(max_length=300)
       projectdetail = models.CharField(max_length=1000)
       User_profiles = models.ForeignKey(User_profiles, on_delete=models.CASCADE)