from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cms.views.show', name='Paginas disponibles'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(.+)', 'cms.views.show_content', name='Vamos a la pagina')
)
