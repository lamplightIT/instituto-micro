from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'engine.views.home', name='home'),
     url(r'^sobre_o_instituto/$', 'engine.views.sobre_o_instituto', name='sobre_o_instituto'),
     url(r'^inscricoes/$', 'engine.views.inscricoes'),
     url(r'^servicos/$', 'engine.views.servicos', name='servicos'),
     url(r'^contato/$', 'engine.views.contato', name='contato'),
    # url(r'^institutomicro/', include('institutomicro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
)