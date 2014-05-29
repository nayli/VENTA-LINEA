from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ejemplo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'usuarios.views.home'),
    url(r'^index/$', 'usuarios.views.index'),
    url(r'^user/nuevo/$', 'usuarios.views.new_users'),
    url(r'^login/$', 'usuarios.views.loged_in'),
    url(r'^perfil/$', 'usuarios.views.perfil'),
    url(r'^cerrar/$', 'usuarios.views.loged_out'),
    url(r'^perfil/new_perfil/$', 'usuarios.views.new_perfil'),
    url(r'^nuevoproducto/$', 'usuarios.views.producto'),
)
