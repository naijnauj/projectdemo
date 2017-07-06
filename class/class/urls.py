"""yuanjian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

import views
from .view import activate
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logreg/', include('logreg.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^regist/', include('regist.urls')),
    url(r'^activate/(?P<code>\w+)',activate),
    #url(r'^article/', include('article.urls')),
	#url(r'^static/(?P<path>.*)S',django.contrib.staticfiles.views.serve),
	url(r'^$',views.index),
]
