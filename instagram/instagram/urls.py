from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

import feedpage.views
import accounts.views

urlpatterns = [
    path('', feedpage.views.index),
    path('admin/', admin.site.urls),
    path('feeds/', include('feedpage.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)