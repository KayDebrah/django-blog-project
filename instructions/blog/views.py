# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

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

class CommentForm(ModelForm):
	class Meta:
		model=Comment
#We exclude comment post to prevent the post from displayin on the commentform and also comment_author from displaying the author's name 
                exclude=['comment_post','comment_author']

@csrf_exempt
def post_detail(request, id, showComments=False):
     posts=Post.objects.get(pk=id)
     comments=Comment.objects.filter(comment_post=id)
     if request.method == 'POST':
          comment=Comment(comment_post=posts)
          #assigning the logged in user to the comment
          comment.comment_author=request.user	
          form = CommentForm(request.POST,instance=comment)
          if form.is_valid():
	       form.save()
	  return HttpResponseRedirect(request.path)
     else:
               form = CommentForm()

     
     t = loader.get_template('blog/post_detail.html')  
     c = Context({'post':posts,'comment':comments,'form':form,'user':request.user })    	
     return HttpResponse(t.render(c))
    	
    #for comment in comments:
	#c = Context({'post':posts,'comment':comment })
    

@csrf_exempt        
def edit_comment(request,id):

     singlecomment=Comment.objects.get(pk=id)
     if request.method == 'POST':
          #comment=Comment(comment_post=singlecomment)	
          form = CommentForm(request.POST,instance=singlecomment)
          if form.is_valid():
	       form.save()
	  return HttpResponseRedirect(singlecomment.comment_post.get_absolute_url())
          #return HttpResponseRedirect(request.path)
     else:
          form = CommentForm(instance=singlecomment)

     t = loader.get_template('blog/edit_comment.html')
     c = Context({'post':singlecomment, 'form':form })
     return HttpResponse(t.render(c))     



    
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

