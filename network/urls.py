from django.conf.urls import patterns, include, url
from network import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'networkForEducation.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       #showmain
                       url(r'^$', views.showMain, name='showMain'),

                       #video operations
                       url(r'^videoPlay/(?P<video_name_slug>[\w\-]+)/$',
                           views.videoPlay, name='videoPlay'),
                       url(r'^videoPage/', views.videoPage, name='videoPage'),
                       url(r'^showSubjectVideos/$', views.showSubjectVideos, name='showSubjectVideos'),

                      #articles operations
                      url(r'^articles/(?P<articles_name_slug>[\w\-]+)/$',views.showArticles,name='showArticles'),
                      url(r'^articlesSelected/(?P<subject_selected_name_slug>[\w\-]+)/$', views.articlesSelected, name='articlesSelected'),
                      url(r'^articlesPage/',views.articlesPage,name='articlesPage'),
                      url(r'^articlesGoodButton/$', views.articlesGoodButton, name='articlesGoodButton'),


                       #test operations
                       url(r'^testPage/', views.testPage, name='testPage'),
                       url(r'^startquestionPage/', views.startquestionPage, name='startquestionPage'),
                       url(r'^questionPage/', views.questionPage, name='questionPage'),
                       
                       #personInfo operations
                       url(r'^personinfo/(?P<personinfo_name_slug>[\w\-]+)/$',
                           views.showPersoninfo, name='showPersoninfo'),
                       url(r'^personinfoPage/', views.personinfoPage,
                           name='personinfoPage'),

                       url(r'^userinfo/', views.showUserInfo, name='showUserInfo'),

                       #register operations
                       url(r'^register/$',views.register,name='register'),
                       url(r'^userLogin/$',views.userLogin,name='userLogin'),
                       )
