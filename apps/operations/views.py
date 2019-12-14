import os
import random

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
from django.db import connection

cursor = connection.cursor()


def add_article():
	''' 一次发5篇'''
	N = 0
	# for (path, dirs, files) in os.walk(r'D:\www\myblog\apps\operations\artfile'):
	for (path, dirs, files) in os.walk(r'/home/ubuntu/Debug/apps/operations/artfile'):
		for file in files:
			con=''
			with open(os.path.join(path, file), 'r') as fr:
				try:
					for line in fr.readlines():
						line=line.replace(' ','&nbsp;')
						con += '<p>'+line+'</p>'
				except Exception as e:
					print('读取异常', e)
					continue
				title = file.split('.')[0]
				add_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
				num = random.choice('123456789')
				sql="insert into `articles_articleinfo`(`title`,`desc`,`content`,`author_id`,`category_id`,`click_num`,`cont_num`,`love_num`,`is_recommend`,`image`,`add_time`) values (" + r"'"+"{}".format(title)+ r"'" + "," + r"'"+"{}".format(title)+ r"'"+ "," + r"'"+"{}".format(con)+ r"'" + ",10,1,0,0,0,0"+ ","+"'article/default"+str(num)+".jpg'"+ "," + r"'"+"{}".format(add_time)+ r"'"+")"
				try:
					cursor.execute(sql)
				except Exception as e:
					print('写入异常', e,title)
					continue
			print(title, '发表成功 ', datetime.datetime.now())
			os.remove(path + '/' + file)
			N += 1
			if N == 1:
				N = 0
				break
	# return JsonResponse({'status': 'faile', 'msg': '内容太短了'})


def add_Marticle():
	''' 每隔6小时发一篇'''
	# for (path, dirs, files) in os.walk(r'D:\www\myblog\apps\operations\artfile'):
	for (path, dirs, files) in os.walk(r'/home/ubuntu/Debug/apps/operations/artfile'):
		for file in files:
			con=''
			with open(os.path.join(path, file), 'r') as fr:
				try:
					for line in fr.readlines():
						line=line.replace(' ','&nbsp;')
						con += '<p>'+line+'</p>'
				except Exception as e:
					print('读取异常', e)
					continue
				title = file.split('.')[0]
				add_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
				num=random.choice('123456789')
				sql="insert into `articles_articleinfo`(`title`,`desc`,`content`,`author_id`,`category_id`,`click_num`,`cont_num`,`love_num`,`is_recommend`,`image`,`add_time`) values (" + r"'"+"{}".format(title)+ r"'" + "," + r"'"+"{}".format(title)+ r"'"+ "," + r"'"+"{}".format(con)+ r"'" + ",10,1,0,0,0,0"+ ","+"'article/default"+str(num)+".jpg'"+ "," + r"'"+"{}".format(add_time)+ r"'"+")"
				try:
					cursor.execute(sql)
				except Exception as e:
					print('写入异常', e,title)
					continue
			print(title, '发表成功 ', datetime.datetime.now())
			os.remove(path + '/' + file)
			break
	# return JsonResponse({'status': 'faile', 'msg': '内容太短了'})
