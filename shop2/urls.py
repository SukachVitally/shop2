from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

print(include('polls.urls'))

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
