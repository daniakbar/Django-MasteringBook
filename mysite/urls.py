"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
#import views.py dari folder mysite beserta objectnya
from mysite.views import homepage, hello, timesnow, hours_ahead, contact
from books import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage), #homepage
    url(r'^hello/$', hello), #hello url
    url(r'^time/$', timesnow),  #time url
    #cara gobloknya
    # url(r'^time/plus/1/$', one_hour_ahead),
    # url(r'^time/plus/2/$', two_hour_ahead),
    # url(r'^time/plus/3/$', three_hour_ahead),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^contact/$', contact),

    # DARI APP books dan folder template
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]
    # if settings.DEBUG:
    #     urlpatterns += [url(r'^debuginfo/$', views.debug),]
