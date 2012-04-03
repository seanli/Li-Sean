from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('core.views',
    # Home Page
    url(r'^$', 'home', name='home'),
)
