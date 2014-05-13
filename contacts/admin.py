
from django.contrib.sites.models import Site 
from django.contrib.auth.models  import *

from django.contrib  import admin
from contacts.models import Contact
from contacts.models import Category
from contacts.models import Action
from contacts.models import Message
from contacts.models import Comment



class ContactAdmin(admin.ModelAdmin):
	search_fields = ['nickname', 'email']
	list_display  = ['nickname', 'email']
        ordering      = ('nickname',)

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['code', 'desc']
	list_display  = ['code', 'desc']
        ordering      = ('code',)

class ActionAdmin(admin.ModelAdmin):
	search_fields = ['code', 'desc']
	list_display  = ['code', 'desc']
        ordering      = ('code',)

class MessageAdmin(admin.ModelAdmin):
	search_fields = ['code', 'desc']
	list_display  = ['code', 'desc']
        ordering      = ('code',)

class CommentInline(admin.TabularInline):
        model = Comment
        extra = 1

class ContactAdmin(admin.ModelAdmin):
        inlines = [CommentInline,]
        search_fields = ['nickname', 'email']
        list_display  = ['nickname', 'email']
        ordering      = ('nickname',)


admin.site.register(Message,  MessageAdmin)
admin.site.register(Contact,  ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Action,   ActionAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

