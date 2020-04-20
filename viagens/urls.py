from django.urls import path
from viagens import views

urlpatterns = [
    path('list/', views.TravelView.as_view(), name='list-travels'),
    path('details/<int:pk>/', views.TravelView.as_view(), name='details-travel'),
]
