from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^callback/', 'upload.views.upload_callback', name='upload_callback'),
)
