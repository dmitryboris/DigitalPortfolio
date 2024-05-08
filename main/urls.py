from django.conf.urls.static import static
from django.urls import path

from dPortfolio import settings
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('dmitry/', views.about, name='dmitry')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
