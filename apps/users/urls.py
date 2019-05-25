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
from django.conf.urls import url
from .views import user_register,user_login,user_logout,user_center
urlpatterns = [
	url(r'^user_register/$',user_register,name='user_register'),
	url(r'^user_login/$',user_login,name='user_login'),
	url(r'^user_logout/$',user_logout,name='user_logout'),
	url('^user_center/$',user_center,name='user_center')
]
