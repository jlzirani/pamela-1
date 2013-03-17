from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'pamela.views.show_macs'),
    (r'^get$', 'pamela.views.get'),
    (r'^set$', 'pamela.views.set'),
)