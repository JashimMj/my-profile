from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    First_Name= models.CharField(max_length=255,null=True,blank=True)
    Last_Name= models.CharField(max_length=255,null=True,blank=True)
    Address = models.CharField(max_length=255,null=True,blank=True)
    Phone = models.CharField(max_length=255,null=True,blank=True)
    Age = models.CharField(max_length=255,null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True)
    Nationality = models.CharField(max_length=255,null=True,blank=True)
    Freelance = models.CharField(max_length=255,null=True,blank=True)
    Langages = models.CharField(max_length=255,null=True,blank=True)
    Working = models.CharField(max_length=255,null=True,blank=True)
    Description=models.CharField(max_length=255,null=True,blank=True)
    Image = models.ImageField(upload_to='User_image', null=True, blank=True)
    Facebook_link=models.CharField(max_length=255,null=True,blank=True)
    twitter_link=models.CharField(max_length=255,null=True,blank=True)
    youtube_link=models.CharField(max_length=255,null=True,blank=True)
    objects=models.Manager()

class working_Experience(models.Model):
    id = models.AutoField(primary_key=True)
    YEARS_OF_EXPERIENCE=models.CharField(max_length=255,null=True,blank=True)
    COMPLETEDPROJECTS=models.CharField(max_length=255,null=True,blank=True)
    HAPPYCUSTOMERS=models.CharField(max_length=255,null=True,blank=True)
    AWARDSWON=models.CharField(max_length=255,null=True,blank=True)
    HTML=models.CharField(max_length=255,null=True,blank=True)
    CSS=models.CharField(max_length=255,null=True,blank=True)
    JAVASCRIPT=models.CharField(max_length=255,null=True,blank=True)
    PYTHON=models.CharField(max_length=255,null=True,blank=True)
    JQUERY=models.CharField(max_length=255,null=True,blank=True)
    PYTHON_DJANGO=models.CharField(max_length=255,null=True,blank=True)
    ORACLE=models.CharField(max_length=255,null=True,blank=True)
    DATABASE=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()


class Experince(models.Model):
    id = models.AutoField(primary_key=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    EXPERIENCE =models.CharField(max_length=255,null=True,blank=True)
    Description=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()

class Educatio(models.Model):
    id = models.AutoField(primary_key=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    Education = models.CharField(max_length=255,null=True,blank=True)
    Description = models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.Education

class project(models.Model):
    id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='projects', null=True, blank=True)
    Link = models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()

class datasend(models.Model):
    id = models.AutoField(primary_key=True)
    Name =models.CharField(max_length=255,null=True,blank=True)
    Email =models.EmailField(max_length=255,null=True,blank=True)
    Subject =models.CharField(max_length=255,null=True,blank=True)
    Description =models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()



