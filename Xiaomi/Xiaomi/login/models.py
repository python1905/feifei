from django.db import models

# Create your models here.
class User(models.Model):
     uid = models.AutoField(primary_key=True)
     username = models.CharField
