from django.conf.urls import patterns, url
from api import views


urlpatterns = patterns('',
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
)
