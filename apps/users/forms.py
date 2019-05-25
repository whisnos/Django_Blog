from django import forms


class RegisterForm(forms.Form):
	email = forms.EmailField(required=True, error_messages={
		'required': '邮箱必填'
	})
	password = forms.CharField(required=True, error_messages={
		'required': '密码必填'
	})
	nick_name = forms.CharField(required=True, error_messages={
		'required': '昵称必填'
	})


class UserLoginForm(forms.Form):
	email = forms.EmailField(required=True, error_messages={
		'required': '邮箱必须填写',
	})
	password = forms.CharField(required=True, error_messages={
		'required': '密码必须填写',
	})
