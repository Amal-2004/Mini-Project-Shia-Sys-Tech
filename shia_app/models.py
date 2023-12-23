from django.db import models

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    status = models.BooleanField(default=False)

class Signin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
class Project(models.Model):
    project_name=models.CharField(max_length=50)
    manager=models.CharField(max_length=50)
    resources=models.PositiveIntegerField()
    male_count=models.PositiveIntegerField()
    female_count=models.PositiveIntegerField()
    progress=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)

 
class projectdetail(models.Model):
    projectname=models.CharField(max_length=250)
    log=models.CharField(max_length=50000,null=True,blank=True)
    

class Edit(models.Model):
    resource_name=models.CharField(max_length=255)
    task=models.CharField(max_length=255)

class File(models.Model):

    project_name=models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'shia_app_file'

    def __str__(self):
        return self.file.name
        
class status_update(models.Model): 
    Status = models.CharField(max_length=255)
    Progress = models.CharField(max_length=255)

    class Meta:
        db_table = 'shia_app_status_update'
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    mobileno = models.CharField(max_length=10,null=True,blank=True)
    emp_id = models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    join_date = models.DateField(null=True,blank=True)
    super_user = models.CharField(max_length=100,null=True,blank=True)
    profile_image_base64 = models.TextField(null=True, blank=True)
