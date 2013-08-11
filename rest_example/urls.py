from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from users.views import UserListAPIView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_example.views.home', name='home'),
    # url(r'^rest_example/', include('rest_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user_list/$', UserListAPIView.as_view(), name='user_list'),
)
