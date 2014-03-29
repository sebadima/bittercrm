


from django.contrib.sites.models import Site 
from django.contrib.auth.models  import *

from django.contrib import admin
from polls.models import Poll



class PollAdmin(admin.ModelAdmin):
	search_fields = ['campo1', 'campo2']
	list_display = ['campo1', 'campo2']

admin.site.register(Poll, PollAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

