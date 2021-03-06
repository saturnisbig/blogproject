"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog.feeds import EntryRSSFeed

urlpatterns = [
    url(r'^adminx/', admin.site.urls),
    url(r'^comments/', include('comments.urls')),
    url(r'^all/rss/$', EntryRSSFeed(), name='rss'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('users.urls', namespace='users')),
    url(r'^', include('blog.urls')),
    url(r'^box/', include('box.urls')),
    # url(r'^api/', include('api.urls')),
    url(r'^tool/', include('tool.urls')),
    url(r'^country/', include('country.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
