from django.db import models

class signup_model(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    class meta:
        db = 'signupmodel'
    
class tasks(models.Model):
    task_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=10 ,null=True)