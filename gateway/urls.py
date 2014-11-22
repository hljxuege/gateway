from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gateway.views.home', name='home'),
    url(r'^gateway/$', 'gateway.views.gateway', name='gateway'),
    url(r'^gateway/method_add/$', 'gateway.views.method_add', name='method-add'),
    # url(r'^gateway/', include('gateway.foo.urls')),
    url(r'^gateway/server_add/$', 'gateway.views.server_add', name='server-add'),
    url(r'^gateway/server_modify/(?P<server_id>\S+)/$', 'gateway.views.server_modify', name='server-modify'),
    url(r'^gateway/server_list/$', 'gateway.views.server_list', name='server-list'),
    url(r'^gateway/servers/$', 'gateway.views.servers', name='servers'),
    
    url(r'^gateway/method_list/$', 'gateway.views.method_list', name='method-list'),
    url(r'^gateway/method_add/$', 'gateway.views.method_add', name='method-add'),
    url(r'^gateway/method_modify/(?P<method_id>\S+)/$', 'gateway.views.method_modify', name='method-modify'),
    
    url(r'^gateway/appkey_list/$', 'gateway.views.appkey_list', name='appkey-list'),
    url(r'^gateway/appkey_modify/(?P<appkey_id>\S+)/$', 'gateway.views.appkey_modify', name='appkey-modify'),
    url(r'^gateway/appkey_add/$', 'gateway.views.appkey_add', name='appkey-add'),
    url(r'^gateway/methods/$', 'gateway.views.methods', name='methods'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^gateway/index/$', 'gateway.views.index', name='index'),
)
