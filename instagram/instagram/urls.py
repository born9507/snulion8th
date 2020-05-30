from django.contrib import admin
from django.urls import path
import feedpage.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', feedpage.views.index, name='index'),
    path('feeds/', include('feedpage.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
