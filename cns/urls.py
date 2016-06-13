"""cns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from notes.views import home, note, note_create, note_edit, note_delete, register, login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^note/(?P<pk>\d+)$', note),
    url(r'^note/(?P<pk>\d+)/edit/$', note_edit),
    url(r'^note/(?P<pk>\d+)/delete/$', note_delete),
    url(r'^note/create/$', note_create),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^logout/', logout),
]
