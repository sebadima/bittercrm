
from django.contrib.sites.models import Site 
from django.contrib.auth.models  import *

from django.contrib import admin
from clienti.models import Clienti
from clienti.models import Categorie



class ClientiAdmin(admin.ModelAdmin):
	search_fields = ['ragione_sociale', 'indirizzo']
	list_display  = ['ragione_sociale', 'indirizzo']

class CategorieAdmin(admin.ModelAdmin):
	search_fields = ['campo1', 'campo2']
	list_display  = ['campo1', 'campo2']

admin.site.register(Clienti, ClientiAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

