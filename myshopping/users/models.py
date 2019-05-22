from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):

     id = models.AutoField(primary_key=True)
     nikename = models.CharField(max_length=255, unique=True, verbose_name="用户昵称")
     age = models.IntegerField(default=18)
     gender = models.CharField(max_length=10, default="男", verbose_name="用户性别")
     avatar = models.ImageField(upload_to='static/image/headers/', default='static/image/headers/pizhi.jpg', verbose_name="用户头像")
     phone = models.CharField(max_length=50, default="15837035590", verbose_name="联系方式")
     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Address(models.Model):

     id = models.AutoField(primary_key=True)
     recv_name = models.CharField(max_length=255, verbose_name="收货人")
     recv_tel = models.CharField(max_length=255, verbose_name="收货人的电话")
     province = models.CharField(max_length=255, verbose_name="收货人的省份")
     city = models.CharField(max_length=255, verbose_name="收货人的城市")
     area = models.CharField(max_length=255, verbose_name="收货人的地区")
     street = models.CharField(max_length=255, verbose_name="收货人街道")
     desc = models.CharField(max_length=255, verbose_name="详情地址描述")
     is_default = models.BooleanField(default=False,verbose_name="是否为默认地址")
     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="地址所属用户")