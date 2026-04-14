from django.urls import path
from .views import ImageListView, ImageDetailView

urlpatterns = [
    path('', ImageListView.as_view(), name='image-list'),
    path('<int:pk>', ImageDetailView.as_view(), name='image-detail'),
]