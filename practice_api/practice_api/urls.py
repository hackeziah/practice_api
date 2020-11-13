"""practice_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views  # for obtain_auth_token setup

from practice_app.views import author_list

from practice_app.views import (
    Blog,
    EntryViewSet,


)  # getting the views here


router = routers.DefaultRouter()

router.register(r'entry', EntryViewSet, basename="entry")

# router.register(r'professions',ProfessionViewSet)
# router.register(r'data-sheet',DataSheetViewSet)
# router.register(r'documents',DocumentViewSet)
# this is for Urls register the ViewSet


urlpatterns = [
    url(r'^api/blog/$', Blog.as_view(), name='blog'),
    url(r'^api/author/$', author_list,  name='author'),
    # url(r'^api/author/(?P<pk>[0-9]+)$', author_detail),

    path('api/', include(router.urls)),

    path('admin/', admin.site.urls),
    path('blog/', Blog.as_view()),

    path('api-auth/', include('rest_framework.urls'))
]
