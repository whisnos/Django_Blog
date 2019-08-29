import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, login, authenticate
from django.db.models import Q

# Create your views here.
from django.urls import reverse

from articles.models import Category, ArticleInfo, TagInfo
from help_tools.Helper import iPagination
from help_tools.format_time import Caltime
from help_tools.send_mail_tools import send_email_code
from users.forms import RegisterForm, UserLoginForm
from users.models import VerifyCodeEmail, UserProfile
from MyBlog.settings import PAGE_SIZE,DISPLAY

def index(request):
	cate_name = Category.objects.all()
	all_category = cate_name.filter(is_tab=True).order_by('-add_time')
	print('all_category',all_category)
	new_articles = ArticleInfo.objects.all().order_by('-usercomment__add_time')
	new_articles = new_articles.order_by('-usercomment__add_time')[:12]
	new_category = [art.category for art in new_articles]
	new_category = set(new_category)
	recommend_article = ArticleInfo.objects.filter(is_recommend=True).order_by('-add_time')[:2]
	all_articles = ArticleInfo.objects.all()
	article_total=all_articles.count()
	page = int((request.GET.get('p',1)))
	all_tags = TagInfo.objects.all()
	today_time=datetime.datetime.now().strftime("%Y-%m-%d")
	all_day=Caltime('2017-12-12',today_time)
	page_params = {
		'total': article_total,
		'page_size': PAGE_SIZE,
		'page': page,
		'display': DISPLAY,
		'url': request.path.replace('&p={}'.format(page),'?')
	}
	pages = iPagination(page_params)
	offset = (page - 1) * PAGE_SIZE
	all_articles=all_articles.order_by('-add_time')[offset:offset+PAGE_SIZE:]
	return render(request, 'index.html', {
		'all_category': all_category,
		'new_articles': new_articles,
		'recommend_article': recommend_article,
		'all_articles': all_articles,
		'all_tags': all_tags,
		'new_category': new_category,
		'pages': pages,
		'all_day':all_day,
		'article_total':article_total,
		'cate_name':cate_name
	})



def user_register(request):
	all_category = Category.objects.filter(is_tab=True).all()
	if request.method == 'GET':
		return render(request, 'user_register.html')
	else:
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			email = register_form.cleaned_data['email']
			pwd = register_form.cleaned_data['password']
			nick_name = register_form.cleaned_data['nick_name']
			user = UserProfile.objects.filter(username=email)
			if user:
				return render(request, 'user_register.html', {
					'msg': '用户名已存在'
				})
			else:
				# if pwd == pwd1:
				new = UserProfile()
				new.username = email
				new.email = email
				new.nick_name = nick_name
				new.set_password(pwd)
				new.save()
				send_email_code(email, '1')
				return render(request, 'wait_start.html', {
					'all_category': all_category,
				})
		# else:
		# 	return render(request, 'user_register.html', {
		# 		'msg': '两次密码不一致'
		# 		})
		else:
			return render(request, 'user_register.html', {
				'register_form': register_form
			})


def user_login(request):
	if request.method == 'GET':
		return render(request, 'user_login.html')
	else:
		loginform = UserLoginForm(request.POST)
		if loginform.is_valid():
			username = loginform.cleaned_data['email']
			password = loginform.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				userobj = UserProfile.objects.filter(username=username)[0]
				if userobj.is_start:
					login(request, user)
					return redirect('/')
				else:
					return HttpResponse('请先去激活账号，在登录')
			else:
				return render(request, 'user_login.html', {
					'msg': '用户名或密码错误'
				})
		else:
			return render(request, 'user_login.html', {
				'loginform': loginform
			})


def user_logout(request):
	logout(request)
	return redirect('/')


def search(request):
	all_category = Category.objects.filter(is_tab=True).all()
	cont = request.GET.get('keyword', '')
	all_articles = ArticleInfo.objects.filter(Q(title__icontains=cont) | Q(desc__icontains=cont)).all()
	new_articles = ArticleInfo.objects.all()
	new_articles = new_articles.order_by('-add_time')[:8]
	all_tags = TagInfo.objects.all()
	if not all_articles:
		return render(request, 'none.html', {
			'all_category': all_category
		})

	return render(request, 'search_list.html', {
		'all_category': all_category,
		'all_articles': all_articles,
		'cont': cont,
		'new_articles': new_articles,
		'all_tags': all_tags
	})


def user_active(request, code):
	if code:
		verifycode = VerifyCodeEmail.objects.filter(code=code)
		if verifycode:
			userobj = UserProfile.objects.filter(email=verifycode[0].email)[0]
			userobj.is_start = True
			userobj.save()
			verifycode.delete()
			return redirect(reverse('user_login'))
		else:
			return render(request, '404.html')
	else:
		return render(request, '404.html')


def user_center(request):
	all_category = Category.objects.filter(is_tab=True).all()
	return render(request, 'center.html', {
		'all_category': all_category
	})
def page_not_found(request):
	return render_to_response('404.html')