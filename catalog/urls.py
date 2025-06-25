from django.urls import path
from .api_views import (
    CarListView, CarDetailView,
    AutopartListView, AutopartDetailView
)
from .views import run_setup

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:id>/', CarDetailView.as_view(), name='car-detail'),
    path('autoparts/', AutopartListView.as_view(), name='autopart-list'),
    path('autoparts/<int:id>/', AutopartDetailView.as_view(), name='autopart-detail'),
    # path('setup/', run_setup),
]
