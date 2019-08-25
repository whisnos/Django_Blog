from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField
# Create your models here.
from users.models import UserProfile
import random

class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name='类别名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	is_tab = models.BooleanField(default=True, verbose_name='是否导航')
	title = models.CharField(max_length=50, verbose_name='类别标题', null=True, blank=True)
	path_name = models.CharField(max_length=15, verbose_name='路径别名', null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '类别表'
		verbose_name_plural = verbose_name

import time

m_y=(time.strftime("%Y"))
m_m=(time.strftime("%m"))



class TagInfo(models.Model):
	name = models.CharField(max_length=20, verbose_name='标签名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	category = models.ForeignKey(Category, verbose_name='所属类别',null=True,blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '标签表'
		verbose_name_plural = verbose_name

class ArticleInfo(models.Model):
	title = models.CharField(max_length=50, verbose_name='标题')
	desc = models.TextField(max_length=80, verbose_name='简介')
	content = UEditorField(verbose_name='文章内容', width=1200, height=400, toolbars='full', imagePath='ueditor/image/'+m_y+'/'+m_m+'/',
                 filePath='ueditor/files/'+m_y+'/'+m_m+'/', upload_settings={'imageMaxSizing': 1024000}, default='')
	click_num = models.IntegerField(default=0, verbose_name='浏览数')
	cont_num = models.IntegerField(default=0, verbose_name='评论数')
	love_num = models.IntegerField(default=0, verbose_name='点赞数')
	image = models.ImageField(upload_to='article/%y/%m/%d', verbose_name='封面', max_length=200,default='article/default'+str(random.choice('12345'))+'.jpg', null=True, blank=True)
	author = models.ForeignKey(UserProfile, verbose_name='文章作者')
	category = models.ForeignKey(Category, verbose_name='所属类别')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
	is_recommend = models.BooleanField(default=False, verbose_name='首页推荐')
	taginfo = models.ForeignKey(TagInfo, verbose_name='所属标签',null=True,blank=True)
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章表'
		verbose_name_plural = verbose_name

# class ArtTag(models.Model):
# 	articleinfo = models.ForeignKey(ArticleInfo, verbose_name='所属文章')
# 	taginfo = models.ForeignKey(TagInfo, verbose_name='所属标签')
# 	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
# 	def __str__(self):
# 		return self.articleinfo.title
#
# 	class Meta:
# 		# 设置字段联合唯一
# 		unique_together = ('articleinfo', 'taginfo')
# 		verbose_name = '文章标签表'
# 		verbose_name_plural = verbose_name


class CommentInfo(models.Model):
	# 谁对谁什么时间操作了什么
	comment_man = models.ForeignKey(UserProfile, verbose_name='评论者')
	comment_article = models.ForeignKey(ArticleInfo, verbose_name='评论文章')
	comment_comment = models.CharField(max_length=200, verbose_name='评论内容')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

	def __str__(self):
		return self.comment_comment

	class Meta:
		verbose_name = '评论表'
		verbose_name_plural = verbose_name
