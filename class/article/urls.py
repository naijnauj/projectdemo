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
from django.conf.urls import  url
from .views import article_list
from .views import article_detail
from .views import ArticleDetailView
from .views import ArticleCreateView

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
    url(r'^detail/(?P<block_id>\d+)', article_detail),
   # url(r'^create/(?P<block_id>\d+)', article_create),
    url(r'^detail_s/(?P<pk>\d+)$', ArticleDetailView.as_view()),
    url(r'^create/(?P<block_id>\d+)', ArticleCreateView.as_view()),
    #url(r'^article/', include('article.urls')),
	#url(r'^static/(?P<path>.*)$',django.contrib.staticfiles.views.serve),
	#url(r'^$',views.index),
]
