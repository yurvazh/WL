from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presents/', views.PresentsView.as_view(), name="presents_list")
]