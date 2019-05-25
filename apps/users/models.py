from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
	nick_name = models.CharField(max_length=20, verbose_name='用户昵称', null=True, blank=True)
	image = models.ImageField(upload_to='user/%y/%m/%d', verbose_name='头像', max_length=200, null=True, blank=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	is_start = models.BooleanField(default=False, verbose_name='是否激活')

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = '用户表'
		verbose_name_plural = verbose_name


class VerifyCodeEmail(models.Model):
	email = models.EmailField(max_length=30, verbose_name='用户邮箱')
	code = models.CharField(max_length=20, verbose_name='验证码')
	code_type = models.CharField(max_length=100,
								 choices=(('1', 'register'), ('2', 'reset'), ('3', 'changeemail'), ('4', 'sendpwd')),
								 verbose_name='验证码类型')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	def __str__(self):
		return self.code

	class Meta:
		verbose_name = '验证码信息表'
		verbose_name_plural = verbose_name
