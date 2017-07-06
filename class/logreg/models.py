from django.db import models


class User(models.Model):
  
  username = models.CharField("用户名",max_length=30)
  password = models.CharField("密码",max_length=30)
  
  
  def __unicode__(self):
      return self.username
	  