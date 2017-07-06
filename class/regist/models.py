from django.db import models

# Create your models here.
class User(models.Model):
  
  username = models.CharField("用户名",max_length=40)
  password = models.CharField("密码",max_length=50)
  email = models.EmailField()
  
  def __str__(self):
      return self.username