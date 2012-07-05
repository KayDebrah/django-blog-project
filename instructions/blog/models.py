from django.db import models

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
	post_create_date=models.DateField()
	post_updated_date=models.DateField()

	def __unicode__(self):
	        return self.post_title

class Comment(models.Model):
	comment_date=models.DateField()
	comment_author=models.CharField(max_length=100)
	comment_body=models.TextField()
	comment_post=models.ForeignKey(Post)

	def __unicode__(self):
	        return self.comment_body


class Reply(models.Model):
	reply_Date=models.DateField()
	author=models.ForeignKey(Author)
	reply_Body=models.CharField(max_length=150)
	reply_Comment=models.ManyToManyField(Comment)
	
	def __unicode__(self):
	        return self.reply_Body


	        



	
