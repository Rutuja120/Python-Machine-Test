from django.urls import path
from .views import (
    ClientListView, ClientCreateView, ClientDetailView,
    ClientUpdateView, ClientDeleteView, ProjectCreateView,
    UserProjectsView, ProjectDeleteView
)

urlpatterns = [
    # Client APIs
    path('clients/', ClientListView.as_view(), name='list-clients'),          # API 1
    path('clients/create/', ClientCreateView.as_view(), name='create-client'), # API 2
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'), # API 3
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='update-client'), # API 4
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='delete-client'), # API 5

    # Project APIs
    path('projects/create/', ProjectCreateView.as_view(), name='create-project'), # API 6
    path('projects/user/', UserProjectsView.as_view(), name='user-projects'), # API 7
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete-project'), # API 8
]
