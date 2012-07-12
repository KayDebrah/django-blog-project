# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""
from django.template import Context, loader
from django.shortcuts import render_to_response

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 

'''
def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

'''
def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))

'''
def post_detail(request, id, showComments=False):
    myresponse=Post.objects.filter(pk=id)
    comments=Comment.objects.filter(comment_post=id)  
    singlecomment=""
    if showComments=="true":
	for post in myresponse:
    		print post
    	for comment in comments:
    		singlecomment="   Post:",post,"</br>","Comment: ",comment
        return HttpResponse(singlecomment)
    else:
        for post in myresponse:
    		print post 
        return HttpResponse(post) 
'''

def post_detail(request, id, showComments=False):
    posts=Post.objects.filter(pk=id)
    comments=Comment.objects.filter(comment_post=id)
    t = loader.get_template('blog/post_detail.html')  
    c = Context({'post':posts,'comment':comments })    	
    return HttpResponse(t.render(c))
    	
    #for comment in comments:
	#c = Context({'post':posts,'comment':comment })
    
        


    
def post_search(request, term):
    results=Post.objects.filter(post_body__contains=str(term))
    t = loader.get_template('blog/post_search.html')
    c = Context({'term':term,'results':results})
    #myresponse='Written by   '+str(author)
    return HttpResponse(t.render(c))


'''
def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
'''

def home(request):
	return render_to_response('blog/base.html',{})

