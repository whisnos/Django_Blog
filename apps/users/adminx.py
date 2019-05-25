from articles.models import Category
from xadmin.views import BaseAdminView, CommAdminView
import xadmin


# class BaseSetting(BaseAdminView):
# 	pass


class ComSetting(object):
	site_footer = '博客系统'
	site_title = '博客管理系统'


xadmin.site.register(CommAdminView, ComSetting)


class CategoryXadmin(object):
	list_display = ['name', 'add_time']




xadmin.site.register(Category, CategoryXadmin)

