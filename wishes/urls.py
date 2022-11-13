from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presents/', views.PresentsView.as_view(), name="presents_list"),
    path('presents/<int:pk>', views.PresentDetailView.as_view(), name="present_info")
]