#encoding=utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	user=models.OneToOneField(User) #对应django提供的User模型,user是userprofile的成员
	website=models.URLField(blank=True)
	picture=models.ImageField(upload_to ='profile_images',blank=True)

	def __unicode__(slef):
		return self.user.username


class Video(models.Model):
	#mid = models.IntegerField(default=0)
	url = models.CharField(max_length=256, default="")
	stage = models.CharField(max_length=128, default="")
	subj = models.CharField(max_length=128, default="")
	name = models.CharField(max_length=128, unique=True, default="")
	title = models.CharField(max_length=128, unique=True, default="")
	count = models.IntegerField(default=0)
	slug = models.SlugField(unique=True, default="")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Video, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name


class Articles(models.Model):
    mid = models.IntegerField(default=0)
    name = models.CharField(max_length=128, default="")
    title = models.CharField(max_length=256, default="")
    subj = models.CharField(max_length=128, default="")
    content = models.CharField(max_length=10000, default="")
    count = models.IntegerField(default=0)
    goodcount = models.IntegerField(default=0)
    comment = models.CharField(max_length=256, default="")
    slug = models.SlugField(unique=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Articles, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
#@guoshijiang the app of project databases design start


class Test(models.Model):
	subj = models.CharField(max_length=128, default="")
	title = models.CharField(max_length=256, default="")
	stage = models.CharField(max_length=128, default="")

	
class Question(models.Model):
 	content=models.CharField(max_length=1280,default="")
	ItemA=models.CharField(max_length=128,default="")
	ItemB=models.CharField(max_length=128,default="")
	ItemC=models.CharField(max_length=128,default="")
	ItemD=models.CharField(max_length=128,default="")
	rightAnswer=models.CharField(max_length=128,default="")
	
#@guoshijiang the app of project databases design end

class  Personinfo(models.Model):
	mid=models.IntegerField(default=0)	
	mstunum=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	sex=models.CharField(max_length=128,default="")
	school=models.CharField(max_length=128,default="")
	grade=models.IntegerField(default=0)	
	age=models.IntegerField(default=0)
	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super(Personinfo,self).save(*args,**kwargs)
	def __unicode__(self):
		return self.name	


class  UserInfo(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	passwd=models.CharField(max_length=128,default="")
	liimit=models.CharField(max_length=128,default="")


class  Comment(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	commentdate=models.DateField()
	commentcontent=models.CharField(max_length=1280,default="")

class  History(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	article=models.CharField(max_length=128,default="")
	video=models.CharField(max_length=128,default="")

class  Subjects(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	count=models.IntegerField(default=0)
	slug=models.SlugField(unique=True,default="")

	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super(Subjects,self).save(*args,**kwargs)
	def __unicode__(self):
		return self.name

class  Stages(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	count=models.IntegerField(default=0)
	slug=models.SlugField(unique=True,default="")

	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super(Stages,self).save(*args,**kwargs)
	def __unicode__(self):
		return self.name