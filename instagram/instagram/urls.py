from django.contrib import admin
from django.urls import path
import feedpage.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/', include('feedpage.urls')),
]
