from django.conf.urls.static import static
from django.urls import path

from dPortfolio import settings
from .views import UserProfileDetailView, about, index, create_achievement, increment_views, increment_likes

urlpatterns = [
    path('', index, name="home"),
    path('dmitry/', about, name='dmitry'),
    path('<slug:slug>/', UserProfileDetailView.as_view(), name='user-detail'),
    path('<slug:slug>/add/', create_achievement, name='add-achievement'),
    path('increment-views/<int:pk>/', increment_views, name='increment-views'),
    path('increment-likes/<int:pk>/', increment_likes, name='increment-likes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
