from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="店铺名称")
    cover = models.ImageField(upload_to="static/image/stroes", default="static/image/stores/qianxi1.jpg", verbose_name="店铺图片")
    intro = models.TextField(verbose_name="店铺描述")
    openTime = models.DateTimeField(auto_now_add=True, verbose_name="开店时间")
    status = models.IntegerField(default=0,verbose_name="店铺状态")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所属用户")
