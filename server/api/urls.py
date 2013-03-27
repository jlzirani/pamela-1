from django.conf.urls import patterns, include, url
from views import getPatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^pamela/', include('pamela.urls')),
    url(r'^api.json$', 'views.getJson'),
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', *getPatterns())


