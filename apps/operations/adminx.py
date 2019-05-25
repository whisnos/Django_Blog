import xadmin
from operations.models import UserComment


class UserCommentXadmin(object):
	list_display = ['comment_man', 'comment_article', 'add_time']


xadmin.site.register(UserComment, UserCommentXadmin)
