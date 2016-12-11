#coding=utf-8

#确保在导入django模块时已经导入了django设置  ,并把环境变量DJANGO_SETTINGS_MODULE设置为项目设置文件
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','networkForEducation.settings')
import random

import django
django.setup()

from network.models import Video,Articles,Question,History,Personinfo,UserInfo,Comment,Subjects,Stages


def testscript():
	subjectss=['adroid','ios','unity3d',]

	#add videos
	'''for i in [x  for x in range(10,20)]:
		add_video(url="http://player.video.qiyi.com/a6c5807899be7e90a243c2956ab2bddb/0/0/w_19rt2shlkl.swf-albumId=5869968409-tvId=5869968409-isPurchase=0-cnId=20",
			stage =random.choice(["primior","junior","senior"]),
			subj=random.choice(subjectss),
			name="videoName"+'%d' %i,
			title="vidoeTitle"+'%d' %i,
			)'''
	#add subjects
	
	for i ,sub in enumerate(subjectss):
		add_subject(mid='%d' %i,
			name=sub,
			)

	
def add_video(url,stage,subj,name,title,count=0):
	v=Video.objects.get_or_create(url=url,stage=stage,subj=subj,name=name,title=title)
	return v

def add_subject(mid,name,count=0):
	v=Subjects.objects.get_or_create(mid=mid,name=name)
	return v



if __name__=='__main__':
	print "starting network population script..."
	testscript()