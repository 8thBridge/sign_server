from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import robertsTest

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^robertsTest/messages$', 'robertsTest.views.all_messages'),
#    url(r'^robertsTest/', include(robertsTest.urls.urlpatterns)),

    # Examples:
    url(r'^$', 'sign_server.views.hello_world'),
    url(r'^miniBoard/$', 'sign_server.views.mini_board'),


    #debug
    url(r'^board_test/$', 'sign_server.views.board_test'),
    url(r'^calibrate_displays/$', 'sign_server.views.calibrate_displays'),
    url(r'^file_test/$', 'sign_server.views.file_test'),
    url(r'^clear_board/$', 'sign_server.views.clear_board'),
    url(r'^time_stamp/$', 'sign_server.views.time_stamp'),



    # url(r'^sign_server/', include('sign_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
