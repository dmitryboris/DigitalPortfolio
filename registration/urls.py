from .views import login_view, RegisterView, UserDetailView
from django.urls import path

urlpatterns = [
    # path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('<str:username>/', login_view, name='user-detail')
]
