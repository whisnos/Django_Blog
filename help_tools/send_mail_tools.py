from django.core.mail import send_mail
from random import randint
from users.models import VerifyCodeEmail
from MyBlog.settings import EMAIL_FROM


def makecode(length):
	code_source = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMzxcvbnmasdfghjklqwertyuiop'
	code = ''
	for i in range(length):
		code += code_source[randint(0, len(code_source) - 1)]
	return code


def send_email_code(e, type):
	code = makecode(8)
	new = VerifyCodeEmail()
	new.email = e
	new.code = code
	new.code_type = type
	new.save()

	send_title = ''
	send_content = ''
	send_type = type
	if send_type == '1':
		send_title = '欢迎注册Debug5'
		send_content = '点击链接激活账号\n http://www.debug5.com/user_active/' + code
		send_mail(send_title, send_content, EMAIL_FROM, [e])
	if send_type == '2':
		send_title = '请重置密码_From Debug5'
		send_content = '点击链接重置密码\n http://www.debug5.com/user/user_reset/' + code
		send_mail(send_title, send_content, EMAIL_FROM, [e])
	if send_type == '3':
		send_title = '请重置邮箱_From Debug5'
		send_content = '请复制验证码去验证:' + code
		send_mail(send_title, send_content, EMAIL_FROM, [e])


def send_pwd(e, type, pwd):
	if type == '4':
		send_title = '您已修改密码'
		send_content = '您的新密码：' + pwd
		send_mail(send_title, send_content, EMAIL_FROM, [e])
