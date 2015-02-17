from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from django.views.generic.base import RedirectView


urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^common/', include('common.urls', namespace="common")),
    url(r'^$' , RedirectView.as_view(pattern_name='common.connexion')),
)
