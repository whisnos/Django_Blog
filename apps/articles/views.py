from django.shortcuts import render, redirect

# Create your views here.
from articles.models import Category, ArticleInfo, ArtTag, TagInfo
from operations.models import UserComment


def list_detail(request, cate):
	all_category = Category.objects.filter(is_tab=True).all()
	cate_queryset = Category.objects.filter(path_name=cate)
	new_articles = ArticleInfo.objects.all()
	new_articles = new_articles.order_by('-add_time')[:8]
	if cate_queryset:
		cate_obj = cate_queryset[0]
		all_articles=cate_obj.articleinfo_set.all()
		# all_tags=cate_obj.taginfo_set.all()
		tag=request.GET.get('tag','')
		if tag:
			# tag_obj=TagInfo.objects.filter(id=int(tag))[0]
			# print(tag_obj)
			# all_articles=tag_obj.arttag_set.
			# print(all_articles)
			# 标签id 通过中间表 找出 所有中间表查询集 就找到所有文章
			art_tag_list=ArtTag.objects.filter(taginfo_id=int(tag))
			if art_tag_list:
				all_articles=[arttag.articleinfo for arttag in art_tag_list]
		return render(request, 'list.html', {
			'all_category': all_category,
			'cate_obj': cate_obj,
			'new_articles': new_articles,
			'all_articles':all_articles
			# 'all_tags':all_tags
		})
	return redirect('/')


def article_detail(request, artid):
	if artid:
		all_category = Category.objects.filter(is_tab=True).all()
		art_queryset = ArticleInfo.objects.filter(id=int(artid))
		new_articles = ArticleInfo.objects.all()
		new_articles = new_articles.order_by('-add_time')[:8]

		if art_queryset:
			art_obj = art_queryset[0]
			art_obj.click_num+=1
			art_obj.save()
			all_tags = TagInfo.objects.all()
			user_comment_list=UserComment.objects.filter(comment_article_id=int(artid))
			return render(request, 'detail.html', {
				'all_category': all_category,
				'art_obj': art_obj,
				'new_articles': new_articles,
				'all_tags':all_tags,
				'user_comment_list':user_comment_list
			})
		else:
			return redirect('/')
