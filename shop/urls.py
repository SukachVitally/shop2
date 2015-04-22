from django.conf.urls import patterns, url
from shop import views


urlpatterns = patterns('',
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^groups/$', views.GroupList.as_view()),
)
