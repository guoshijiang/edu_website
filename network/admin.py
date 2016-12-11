from django.contrib import admin
from network.models import Video,Articles,Test,Question,History,Personinfo,UserInfo,Comment,Subjects,UserProfile
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
	#list_display = ('title', 'category', 'url')
	prepopulated_fields={'slug':('name',)}

class ArticlesAdmin(admin.ModelAdmin):
	#list_display = ('title', 'category', 'url')
	prepopulated_fields={'slug':('name',)}

admin.site.register(Video,VideoAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(History)
admin.site.register(Personinfo)
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Subjects)