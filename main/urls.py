from django.conf.urls.static import static
from django.urls import path

from dPortfolio import settings
from .views import UserDetailView, about, index

urlpatterns = [
    path('', index, name="home"),
    path('dmitry/', about, name='dmitry'),
    path('<slug:username>/', UserDetailView.as_view(), name='user-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
