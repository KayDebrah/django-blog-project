"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^$', 'blog.views.home'),
    #url(r'^blog/posts/$', 'blog.views.post_list'),
    url(r'^login/$','reg.views.do_login'),
    url(r'^logout/$','reg.views.do_logout'),
    ## add your url here
    #url(r'^posts/search/(?P<term>\w+)/$', 'blog.views.post_search'),
    

)
