from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^blog/$', 'blog', name='blog'),
    url(r'^blog/(?P<post_id>\d+)/$', 'blog'),
)
