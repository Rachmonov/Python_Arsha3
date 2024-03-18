from django.contrib import admin
from myfolder.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Type,AdminType)


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','type','client','date','url','text','picture1','picture2','picture3']

admin.site.register(Portfolio,AdminPortfolio)






class AdminPosition(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Position,AdminPosition)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'name','position','text','picture1','picture2','picture3','picture4','picture5']


admin.site.register(Team,AdminTeam)


class AdminServices(admin.ModelAdmin):
    list_display = ['id','name','text','picture1']

admin.site.register(Services,AdminServices)


class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','gmail','subject','message']

admin.site.register(Contact,AdminContact)


class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id','gmail']

admin.site.register(Subscribe,AdminSubscribe)