from .views import register, login, profile_view, password_reset, RegisterView
from django.urls import path

urlpatterns = [
    # path('password_reset/', password_reset, name='password_reset'),
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
]
