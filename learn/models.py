from django.db import models

class signup_model(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    class meta:
        db = 'signupmodel'
    
