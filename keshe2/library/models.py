from django.db import models

# Create your models here.

# blank：设置为True时，字段可以为空。设置为False时，字段是必须填写的。字符型字段CharField和TextField是用空字符串来存储空值的。
# verbose_name：就是在后台显示对对应的名称。表示给字段取一个可读的名字。
#                                   若设置user字段的verbose_name为用户名，在模型中，可以很直观的看到这个字段表示是什么。



# 用户表
class user(models.Model):
    avatar = models.CharField(max_length=100,verbose_name="头像",blank=True)
    account=models.CharField(max_length=30,verbose_name="账号",primary_key=True)
    password=models.CharField(max_length=30,verbose_name="密码")
    sex=models.CharField(max_length=30,verbose_name="性别",blank=True)


# 图书馆座位表
class classroom(models.Model):
    # place_number = models.CharField(max_length=100,verbose_name="座位号",primary_key=True)
    # freeTime=models.CharField(max_length=30,verbose_name="可预约时间",blank=True,)
    # userId=models.CharField(max_length=30,verbose_name="预约者学号",blank=True,)
    # busy=models.CharField(max_length=30,verbose_name="是否忙碌")

    place_id = models.CharField(max_length=30,verbose_name="座位id",primary_key=True)
    place_number = models.CharField(max_length=100,verbose_name="座位号")
    busy =models.CharField(max_length=30,verbose_name="是否忙碌")

# 预约信息表
class reservation(models.Model):  
    id=models.CharField(max_length=30,verbose_name="学号",primary_key=True)
    name=models.CharField(max_length=30,verbose_name="姓名")
    place=models.CharField(max_length=50,verbose_name="预约座位")
    time=models.CharField(max_length=50,verbose_name="预约时间")
