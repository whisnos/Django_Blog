import os

from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from articles.models import ArticleInfo, Category
from operations.forms import UserCommentForm
from operations.models import UserComment
from users.models import UserProfile


def user_comment(request, artid):
	commentform = UserCommentForm(request.POST)
	if commentform.is_valid():
		content = commentform.cleaned_data['content']
		# nick_name = commentform.cleaned_data['nick_name']
		if request.user.is_authenticated:
			user_com = UserComment()
			user_com.comment_man = request.user
			user_com.content = content
			user_com.comment_article_id = artid
			user_com.save()
			art_obj = ArticleInfo.objects.filter(id=int(artid))[0]
			art_obj.cont_num += 1
			art_obj.save()
			# request.user.nick_name = nick_name
			# request.user.save()
			return JsonResponse({'status': 'ok', 'msg': '评论成功', 'content': content})
		return JsonResponse({'status': 'faile', 'msg': '请登录再评论'})
	return JsonResponse({'status': 'faile', 'msg': '内容太短了'})

import datetime
def add_article():
	''' 一次发5篇'''
	a=UserProfile.objects.filter(id=10).first()
	c=Category.objects.filter(id=1).first()
	# for (path, dirs, files) in os.walk(r'D:\www\myblog\apps\operations\artfile'):
	N=0
	for (path, dirs, files) in os.walk(r'/home/Debug/MyBlog/apps/operations/artfile'):
		print('files', files)
		for file in files:
			ART = ArticleInfo()
			with open(os.path.join(path, file), 'r+') as fr:
				try:
					ART.content = fr.read()
				except Exception as e:
					print('读取异常',e)
					continue
				ART.desc=ART.title=file.split('.')[0]
				ART.author = a
				ART.category = c
				ART.save()
			print(ART.title,'发表成功 ',datetime.datetime.now())
			os.remove(path + '/' + file)
			N+=1
			if N ==5:
				N=0
				break
def add_Marticle():
	''' 每隔6小时发一篇'''
	a=UserProfile.objects.filter(id=10).first()
	c=Category.objects.filter(id=1).first()
	# for (path, dirs, files) in os.walk(r'D:\www\myblog\apps\operations\artfile'):
	for (path, dirs, files) in os.walk(r'/home/Debug/MyBlog/apps/operations/artfile'):
		print('files', files)
		for file in files:
			ART = ArticleInfo()
			with open(os.path.join(path, file), 'r+') as fr:
				try:
					ART.content = fr.read()
				except Exception as e:
					print('读取异常',e)
					continue
				ART.desc=ART.title=file.split('.')[0]
				ART.author = a
				ART.category = c
				ART.save()
			print(ART.title,'发表成功 ',datetime.datetime.now())
			os.remove(path + '/' + file)
			break