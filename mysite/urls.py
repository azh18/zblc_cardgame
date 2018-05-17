"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from card import views

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'hello/$', views.say_hello),
    url(r'index/$', views.flush),
    url(r'login/$', views.login),
    url(r'test/$', views.test),
    url(r'get_wupin_card_pile/$', views.get_wupin_card_pile),
    url(r'get_ziyuan_card_pile/$', views.get_ziyuan_card_pile),
    url(r'get_consider/$', views.get_card_from_consider),
    url(r'use/$', views.use_card),
    url(r'drop_consider/$', views.drop_consider),
    url(r'buy/$', views.buy),
    url(r'drop/$', views.drop_card),
    url(r'add_score/$', views.add_score),
    url(r'sub_score/$', views.sub_score),
    url(r'^$', views.login),
]
