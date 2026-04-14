from django.urls import path
from .views import AnnotationListView, AnnotationDetailView

urlpatterns = [
    path('<int:image_id>', AnnotationListView.as_view(), name='annotation-list'),
    path('detail/<int:pk>', AnnotationDetailView.as_view(), name='annotation-detail'),
]