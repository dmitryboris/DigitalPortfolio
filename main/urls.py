from django.conf.urls.static import static
from django.urls import path

from dPortfolio import settings
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('dmitry/', about, name='dmitry'),
    path('<slug:slug>/', UserProfileDetailView.as_view(), name='user-detail'),
    path('<slug:slug>/add/', create_achievement, name='add-achievement'),
    path('increment-views/<int:pk>/', increment_views, name='increment-views'),
    path('toggle-like/<int:pk>/', toggle_like, name='toggle-like'),
    path('profile/<slug:slug>/update/', update_profile, name='update-profile'),
    path('redirect-home/<int:pk>/', redirect_home, name='redirect-home'),
    path('achievements/<int:pk>/', achievement_detail, name='achievement-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
