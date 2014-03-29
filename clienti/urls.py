
from django.conf.urls import patterns, url

from clienti.views import PublisherList
from clienti import views


urlpatterns = patterns('',
    url(r'^$'                  , views.index,  name='index' ),
    url(r'^(?P<poll_id>\d+)/$' , views.detail, name='detail'),
    url(r'^pippo/$'             , views.pippo,  name='pippo' ),
)
