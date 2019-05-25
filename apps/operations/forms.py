from django import forms


class UserCommentForm(forms.Form):
	# nick_name = forms.CharField(required=True, error_messages={
	# 	'required': '内容必填',
	# })
	content = forms.CharField(required=True, min_length=5, max_length=200, error_messages={
		'required': '内容必填',
		'min_length': '最小5个字符',
		'max_length': '内容过长'
	})
