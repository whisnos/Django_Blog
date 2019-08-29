from django.shortcuts import render, redirect

# Create your views here.
from MyBlog.settings import PAGE_SIZE, DISPLAY
from articles.models import Category, ArticleInfo, TagInfo
from help_tools.Helper import iPagination
from operations.models import UserComment


def list_detail(request, cate):
	all_category = Category.objects.filter(is_tab=True).order_by('add_time')
	cate_queryset = Category.objects.filter(path_name=cate)
	new_articles = ArticleInfo.objects.all()
	new_articles = new_articles.order_by('-add_time')[:8]
	if cate_queryset:
		page = int((request.GET.get('p', 1)))
		cate_obj = cate_queryset[0]
		tag = request.GET.get('tag', '')
		if tag:
			import re
			if not re.match(r'[1-9]\d*', tag):
				return redirect('/')
			all_articles = ArticleInfo.objects.filter(taginfo_id=int(tag))
			article_total = all_articles.count()
			page_params = {
				'total': article_total,
				'page_size': PAGE_SIZE,
				'page': page,
				'display': DISPLAY,
				'url': request.path.replace('&p={}'.format(page), '?')
			}
			pages = iPagination(page_params)
			offset = (page - 1) * PAGE_SIZE
			all_articles = all_articles.order_by('-add_time')[offset:offset + PAGE_SIZE:]
			return render(request, 'list.html', {
				'all_category': all_category,
				'cate_obj': cate_obj,
				'new_articles': new_articles,
				'all_articles': all_articles,
				'pages': pages,
				'tagnum': (tag)
			})
		else:
			all_articles = cate_obj.articleinfo_set.all()
			page = int((request.GET.get('p', 1)))
			if tag:
				import re
				if not re.match(r'[1-9]\d*', tag):
					return redirect('/')
				all_articles = ArticleInfo.objects.filter(taginfo_id=int(tag))
			article_total = all_articles.count()
			page_params = {
				'total': article_total,
				'page_size': PAGE_SIZE,
				'page': page,
				'display': DISPLAY,
				'url': request.path.replace('&p={}'.format(page), '?')
			}
			pages = iPagination(page_params)
			offset = (page - 1) * PAGE_SIZE
			all_articles = all_articles.order_by('-add_time')[offset:offset + PAGE_SIZE:]
			return render(request, 'list.html', {
				'all_category': all_category,
				'cate_obj': cate_obj,
				'new_articles': new_articles,
				'all_articles': all_articles,
				'pages': pages,
				'tagnum': (tag)
			})
	return redirect('/')


def article_detail(request, artid):
	if artid:
		all_category = Category.objects.filter(is_tab=True).order_by('add_time')
		art_queryset = ArticleInfo.objects.filter(id=int(artid))
		new_articles = ArticleInfo.objects.all().order_by('-add_time')[:8]

		if art_queryset:
			art_obj = art_queryset[0]
			art_obj.click_num += 1
			art_obj.save()
			all_tags = TagInfo.objects.all()
			user_comment_list = UserComment.objects.filter(comment_article_id=int(artid))
			# cate_name = Category.objects.all()
			return render(request, 'detail.html', {
				'all_category': all_category,
				'art_obj': art_obj,
				'new_articles': new_articles,
				'all_tags': all_tags,
				'user_comment_list': user_comment_list,
				# 'cate_name': cate_name
			})
		else:
			return redirect('/')
