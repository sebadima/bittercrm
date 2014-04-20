
from django.contrib.sites.models import Site 
from django.contrib.auth.models  import *

from django.contrib  import admin
from contacts.models import Contact
from contacts.models import Category
from contacts.models import Action



class ContactAdmin(admin.ModelAdmin):
	search_fields = ['nickname', 'email']
	list_display  = ['nickname', 'email']

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['code', 'desc']
	list_display  = ['code', 'desc']

class ActionAdmin(admin.ModelAdmin):
	search_fields = ['code', 'desc']
	list_display  = ['code', 'desc']

admin.site.register(Contact,  ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Action,   ActionAdmin)

