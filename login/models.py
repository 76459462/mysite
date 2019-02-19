from django.db import models

# Create your models here.
#创建models 定义字段类型 字段长度
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)