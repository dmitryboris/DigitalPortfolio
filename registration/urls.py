from .views import RegisterView, UserDetailView
from django.urls import path

urlpatterns = [
    # path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('<slug:username>/', UserDetailView.as_view(), name='user-detail')
]
