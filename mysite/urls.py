from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^clienti/', include('clienti.urls')),
    url('^$', TemplateView.as_view(template_name='index.html')),
    url('^about$', TemplateView.as_view(template_name='about.html')),
    url('^lancio$', TemplateView.as_view(template_name='lancio.html')),
    url(r'^admin/', include(admin.site.urls)),
)
