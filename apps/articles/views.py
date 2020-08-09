from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from MyBlog.settings import PAGE_SIZE, DISPLAY, EMAIL_FROM
from articles.models import Category, ArticleInfo, TagInfo
from help_tools.Helper import iPagination
from operations.models import UserComment
import random

def list_detail(request, cate):
	all_category = Category.objects.filter(is_tab=True).order_by('add_time')
	cate_queryset = Category.objects.filter(path_name=cate)
	new_articles = ArticleInfo.objects.all()
	new_articles = new_articles.order_by('-id')[:8]
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

the_list = ["周杰伦", "蔡依林", "莫文蔚bai", "冯德伦", "萧亚轩du", "徐若瑄", "周渝民", "吴建豪", "朱孝天", "孙楠", "张柏芝zhi", "谢霆锋", "孙俪", "邓超dao",
            "马伊俐", "文章", "关之琳", "吴佩慈", "佟大为", "关悦", "那英", "王菲", "苏有朋", "李亚鹏", "周迅", "古巨基", "谭咏麟", "巩俐", "章子怡", "范冰冰",
            "李冰冰", "李小璐", "王珞丹", "胡军", "刘德华", "黎明", "郭富城", "张学友", "成龙", "韩庚", "汪东城", "吴尊", "陈乔恩", "宋慧乔", "何润东", "蔡卓妍",
            "刘亦菲", "王力宏", "梁静茹", "王光良", "罗大佑", "周华健", "李宗盛", "齐秦", "萧蔷", "陈小春", "陈晓东", "应采儿", "黄晓明", "方力申", "伍思凯",
            "温兆伦", "言承旭", "陈浩民", "立威廉", "金城武", "李连杰", "孙红雷", "蒲巴甲", "罗中旭", "韩红", "陈红", "徐帆", "蒋雯丽", "屠洪刚", "濮存昕", "许晴",
            "林俊杰", "王心凌", "杜德伟", "林子祥", "谭耀文", "张卫健", "罗嘉良", "费玉清", "张雨生", "徐静蕾", "潘玮柏", "陶喆", "陈奕迅", "范逸臣", "方力申",
            "周慧敏", "曹格", "苏永康", "吴奇隆", "曾志伟", "曾宝仪", "童安格", "安以轩", "杨丞琳", "郑秀文", "梁咏琪", "胡杏儿", "黄宗泽", ]
def article_detail(request, artid):
	if artid:
		all_category = Category.objects.filter(is_tab=True).order_by('add_time')
		art_queryset = ArticleInfo.objects.filter(id=int(artid))
		new_articles = ArticleInfo.objects.all().order_by('-id')[:8]

		if art_queryset:
			username = random.choice(the_list)
			art_obj = art_queryset[0]
			art_obj.click_num += 1
			art_obj.save()
			all_tags = TagInfo.objects.all().order_by('id')
			user_comment_list = UserComment.objects.filter(comment_article_id=int(artid))
			# cate_name = Category.objects.all()
			return render(request, 'detail.html', {
				'all_category': all_category,
				'art_obj': art_obj,
				'new_articles': new_articles,
				'all_tags': all_tags,
				'user_comment_list': user_comment_list,
				'username':username,
				# 'cate_name': cate_name
			})
		else:
			return redirect('/')


def weixin_handler(request):
	print(111111111,request.GET)
	send_mail(str(request.GET), str(request.GET), EMAIL_FROM, ['853307553@qq.com'])
	# signature = request.GET.get("signature",1)  # 先获取加密签名
	# timestamp = request.GET.get("timestamp",1)  # 先获取加密签名
	# nonce = request.GET.get("nonece",1)  # 获取随机数
	echostr = request.GET.get("echostr")  # 获取随机字符串
	token = "wurong"  # 自己设置的token
	# 使用字典序排序（按照字母或数字的大小顺序进行排序）
	return HttpResponse(echostr)