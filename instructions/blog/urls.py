"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    #url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$','blog.views.post_detail', name='post_detail'),
    #url(r'^posts/edit_comment/(?P<id>\d+)/edit/$','blog.views.edit_comment', name='edit_comment'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail', name='post_detail'),
    url(r'^posts/edit_comment/(?P<id>\d+)/edit/$', 'blog.views.edit_comment', name='edit_comment'),
    ## add your url here
    url(r'^posts/search/(?P<term>\w+)/$', 'blog.views.post_search'),
    

)
