from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('users/', views.UserListView.as_view(), name="wishlists")
]