from django.conf.urls.static import static
from django.urls import path

from dPortfolio import settings
from .views import UserProfileDetailView, about, index, create_achievement

urlpatterns = [
    path('', index, name="home"),
    path('dmitry/', about, name='dmitry'),
    path('<slug:slug>/', UserProfileDetailView.as_view(), name='user-detail'),
    path('<slug:slug>/add/', create_achievement, name='add-achievement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
