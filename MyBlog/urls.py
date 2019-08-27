"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from users.views import index,search,user_active,page_not_found
from articles.views import list_detail,article_detail
from operations.views import user_comment,add_Marticle
import xadmin
urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^ueditor/',include('DjangoUeditor.urls')),
	url(r'^mysite/',xadmin.site.urls),
	url(r'^user/',include('users.urls')),
	url(r'^list/(\w+)/$',list_detail,name='list'),
	url(r'^detail/(\d+)/$',article_detail,name='detail'),
	url(r'^search/$',search,name='search'),
	url(r'^user_active/(\w+)/$',user_active,name='user_active'),
	url(r'^user_comment/(\d+)/$',user_comment,name='user_comment'),
	# url(r'^add_article/$', add_Marticle, name='add_article')
]
handler404 = page_not_found #改动2