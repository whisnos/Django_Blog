from django.db import models
from datetime import datetime
# Create your models here.
from articles.models import ArticleInfo
from users.models import UserProfile


class UserComment(models.Model):
	comment_man = models.ForeignKey(UserProfile, verbose_name="评论人")
	comment_article = models.ForeignKey(ArticleInfo, verbose_name="评论课程")
	content = models.CharField(max_length=300, verbose_name="评论内容")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

	def __str__(self):
		return self.comment_man.email

	class Meta:
		verbose_name = '用户评论信息表'
		verbose_name_plural = verbose_name
