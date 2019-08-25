import xadmin
from articles.models import TagInfo, ArticleInfo


class TagInfoXadmin(object):
	list_display = ['name', 'category','add_time']
	list_filter = ['category']

# class ArtTagXadmin(object):
# 	list_display = ['articleinfo', 'taginfo', 'add_time']


class ArticleInfoXadmin(object):
	list_display = ['title', 'click_num', 'cont_num', 'author', 'category', 'add_time']
	style_fields = {'content': 'ueditor'}
	search_fields = ['title']
	# 添加附加选项表
	# class ArtTagInlines(object):
	# 	model = ArtTag
	# 	style = 'tab'
	# 	# exclude=['add_time']
	# 	extra = 2
	#
	# inlines = [ArtTagInlines]


xadmin.site.register(TagInfo, TagInfoXadmin)
# xadmin.site.register(ArtTag, ArtTagXadmin)
xadmin.site.register(ArticleInfo, ArticleInfoXadmin)
