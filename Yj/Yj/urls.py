from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#url(r'^static/(?P<path>,*)$',django.contrib.staticfiles.views.serve),
    url(r'^$',views.index),
)     
    
