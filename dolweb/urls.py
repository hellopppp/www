from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Monkey patching ftw...
import dolweb.utils.monkey

admin.autodiscover()

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'dolweb.homepage.views.home', name='home'),

    # Media (image gallery, link to videos)
    url(r'^media/', include('dolweb.media.urls')),

    # Documentation (FAQ and guides)
    url(r'^docs/', include('dolweb.docs.urls')),

    # Downloads
    url(r'^download/', include('dolweb.downloads.urls')),

    # Blog
    url(r'^blog/', include('dolweb.blog.urls')),

    # Compatibility list
    url(r'^compat/', include('dolweb.compat.urls')),

    # Django administration
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
