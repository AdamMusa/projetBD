from django.urls import path
from django.views.generic.base import RedirectView
from app.views import (
    StudyListView,
    StudyCreateUpdateView,
    StudyDeleteView,
    IndexView
)
app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('studies/', StudyListView.as_view(), name='list'),
    path('study/add/', StudyCreateUpdateView.as_view(), name='create'),
    path('study/<int:pk>/edit/', StudyCreateUpdateView.as_view(), name='edit'),
    path('study/<int:pk>/delete/', StudyDeleteView.as_view(), name='delete')
]
