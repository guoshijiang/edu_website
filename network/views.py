#encoding=utf-8
from django.shortcuts import render
from network.models import Video,Articles,Test,Question,History,Personinfo,UserInfo,Comment,Subjects,Stages
from network.forms import UserForm,UserProfileForm
# Create your views here.
from django.http import HttpResponse
from django.core import serializers#for serlize json

########.....................waiting  for  fullfill....................####
def showMain(request):	
	context_dict={}
	video_list1=Video.objects.all()[:8]
	video_list2=Video.objects.all()[8:16]
	context_dict['categories1']=video_list1
	context_dict['categories2']=video_list2
	return render(request,'network/index.html',context_dict)

def videoPage(request):
	context_dict={}
	video_list=Video.objects.all()
	subject_list= Subjects.objects.all()
	context_dict['subjects']=subject_list
	context_dict['categories']=video_list
	return render(request,'network/video.html',context_dict)

def videoPlay(request,video_name_slug):
	context_dict={}
	try:
		videoItem=Video.objects.get(slug = video_name_slug)
		videoItem.count=videoItem.count+1
		videoItem.save()    # save count   666666666
		context_dict['video_name']=videoItem.name
		context_dict['video_urls']=videoItem.url
		context_dict['video']=videoItem
	except Video.DoesNotExist:
		print 'video none'
	return render(request,'network/videoPlay.html',context_dict)

def showSubjectVideos(request):
	param=request.GET.get('subj')
	if param!=404:
		data1=serializers.serialize("json",Video.objects.filter(subj = param))
	else:
		data1={}
	return HttpResponse(data1)



def articlesPage(request):
    context_dict = {}
    articles_list = Articles.objects.all()
    subject_list = Subjects.objects.all()
    context_dict['subjects'] = subject_list
    context_dict['categories'] = articles_list
    return render(request, 'network/articles.html', context_dict)


# articles operations#######################
def articlesSelected(request, subject_selected_name_slug):
    context_dict = {}

    subject_list = Subjects.objects.all()
    context_dict['subjects'] = subject_list
    articles_list = Articles.objects.filter(subj=subject_selected_name_slug)
    context_dict['categories'] = articles_list
    return render(request, 'network/articles.html', context_dict)


def showArticles(request, articles_name_slug):
    articles_dict = {}
    try:
        articlesItem = Articles.objects.get(slug=articles_name_slug)
        articlesItem.count = articlesItem.count + 1
        articlesItem.save()
        articles_dict['articles_title'] = articlesItem.title
        articles_dict['articles_name'] = articlesItem.name
        articles_dict['articles'] = articlesItem
        articles_dict['articles_subj'] = articlesItem.subj
    except Articles.DoesNotExist:
        print 'articles none'
    return render(request, 'network/articlesPage.html', articles_dict)


def articlesGoodButton(request):
    param = request.GET.get('name')
    articlesItem = Articles.objects.get(name=param)
    articlesItem.goodcount = articlesItem.goodcount + 1
    articlesItem.save()
    return HttpResponse(articlesItem)


#@guoshijiang this module is mine start
def testPage(request):
	return render(request,'network/test.html')

def startquestionPage(request):
	test_list=Test.objects.all()
	test_dict={'categories':test_list}
	return render(request,'network/startquestion.html',test_dict)

def questionPage(request):
	question_list=Question.objects.all()
	question_dict={'categories':question_list}
	return render(request,'network/question.html',question_dict)

#@guoshijiang this module is mine end
def personinfoPage(request):
	personinfo_list=Personinfo.objects.all()
	personinfo_dict={'categories':personinfo_list}
	return render(request,'network/personinfo.html',personinfo_dict)
def showPersoninfo(request,personinfo_name_slug):
	personinfo_dict={}
	try:
		personinfoItem=Personinfo.objects.get(slug = personinfo_name_slug)
		personinfo_dict['personinfo_name']=personinfoItem.name
		personinfo_dict['personinfo']=personinfoItem
	except Personinfo.DoesNotExist:
		print 'personinfo none'
	return render(request,'network/personinfo.html',personinfo_dict)

def showUserInfo(request):
	return render(request,'network/userinfo.html')

########.....................waiting  for  append ....................####



###################user forms##################
#注册函数
def register(request):
	registered=False
	#如果是post请求
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user =user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user

			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']

			profile.save()
			registered=True
		else:
			print user_form.errors,profile_form.errors
	#如果是get请求
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render(request,'network/register.html',
			{
				'user_form':user_form,
				'profile_form':profile_form,
				'registered':registered,
			}
		)


#登陆函数
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect

def userLogin(request):
	if request.method=='POST':
		username =request.POST.get('username')
		password = request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user) #django自己的登陆函数
				return HttpResponseRedirect('/network/')#登陆成功跳转页面
									#返回代码302,表示重定向
			else:
				return HttpResponse("your account is invalid")
		else:
			print 'Invalid login details:{0},{1}'.format(username,password)
			return HttpResponse("Invalid login") #注意失败返回
			#print 'Invalid login details:%s,%s' %(username,password)
	else:
		return render(request,'network/userLogin.html')