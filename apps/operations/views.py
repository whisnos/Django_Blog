from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from articles.models import ArticleInfo
from operations.forms import UserCommentForm
from operations.models import UserComment
from users.models import UserProfile


def user_comment(request,artid):
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
			return JsonResponse({'status': 'ok', 'msg': '评论成功','content':content})
		return JsonResponse({'status': 'faile', 'msg': '请登录再评论'})
	return JsonResponse({'status': 'faile', 'msg': '内容太短了'})