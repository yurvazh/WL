from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presents/', views.PresentsView.as_view(), name="presents_list"),
    path('presents/<int:p_id>', views.presentdetailview, name="present_info"),
    path('wishlist/<int:us_id>', views.show_wishlist, name="WLbyUser"),
    path('presents/<int:pk>/update', views.PresentUpdateView.as_view(), name="update"),
    path('presents/create', views.PresentCreateView.as_view(), name="create"),
    path('presents/<int:pk>/delete', views.PresentDeleteView.as_view(), name="delete")
]