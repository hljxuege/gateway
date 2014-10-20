from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gateway.views.home', name='home'),
    url(r'^gateway/$', 'gateway.views.gateway', name='gateway'),
    url(r'^gateway/method_add/$', 'gateway.views.method_add', name='method-add'),
    # url(r'^gateway/', include('gateway.foo.urls')),
    url(r'^gateway/server_add/$', 'gateway.views.server_add', name='server-add'),
    url(r'^gateway/server_modify/(?P<server_id>\S+)/$', 'gateway.views.server_modify', name='server-modify'),
    url(r'^gateway/server_list/$', 'gateway.views.server_list', name='server-list'),
    
    url(r'^gateway/method_list/$', 'gateway.views.method_list', name='method-list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^gateway/index/$', 'gateway.views.index', name='index'),
)
