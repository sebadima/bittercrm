
from django.conf.urls import patterns, url

from contacts.views import PublisherList
from contacts import views


urlpatterns = patterns('',
    url(r'^$'                      , views.index               , name='index'    ),
    url(r'^mailing/$'              , views.mailing             , name='mailing'    ),
    url(r'^candidates/$'           , views.candidates          , name='candidates'),
    url(r'^prova/$'           , views.prova          , name='prova'),
)
