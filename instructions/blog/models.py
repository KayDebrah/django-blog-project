from django.db import models
import re
from django.contrib import admin

# Create your models here.

class Category(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField()
	def __unicode__(self):
		return self.title

class Author(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	
	def __unicode__(self):
	        return self.name



class Post(models.Model):
	post_title=models.CharField(max_length=50)	
	post_author=models.ForeignKey(Author)
	post_body=models.TextField()
	category=models.ForeignKey(Category)
	post_create_date=models.DateField(auto_now="True")
	post_updated_date=models.DateField()

	def __unicode__(self):
	        return self.post_title
	
	def limit_post(self):
	        return self.post_body[:60]

       
	def get_absolute_url(self):
		return "/blog/posts/%i/true" % self.id

'''
	@models.permalink
	def get_absolute_url(self):
		return ('post_detail',(),{'id':self.id,'showComments':'true/'})

'''

	
	


'''
class PostInline(admin.TabularInline):
		model = Post

class AuthorAdmin(admin.ModelAdmin):
		inlines = [PostInline]

'''



class Comment(models.Model):
	comment_date=models.DateField(auto_now="True")
	comment_author=models.CharField(max_length=100)
	comment_body=models.TextField()
	comment_post=models.ForeignKey(Post)

	def __unicode__(self):
	        return self.comment_body
	def limit_body(self):
	        return self.comment_body[:60]

	
class CommentInline(admin.TabularInline):
	model=Comment	
	#list_display=('post_title','post_author','post_create_date','post_updated_date')
	#list_filter = ('post_create_date',)

class PostAdmin(admin.ModelAdmin):
		list_display = ('post_title', 'post_create_date','post_updated_date')
		list_filter = ('post_create_date',)
		#ordering = ('-publication_date')
		search_fields = ('post_title',)
		inlines = [CommentInline]

#
class CommentAdmin(admin.ModelAdmin):
	list_display=('comment_post','limit_body','comment_author','comment_date',)
	list_filter = ('comment_date','comment_author',)

class Reply(models.Model):
	reply_Date=models.DateField()
	author=models.ForeignKey(Author)
	reply_Body=models.CharField(max_length=150)
	reply_Comment=models.ManyToManyField(Comment)
	
	def __unicode__(self):
	        return self.reply_Body


	        



	
