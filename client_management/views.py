from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import (
    ClientSerializer, ProjectSerializer,
    ClientDetailSerializer
)

# API 1: List all clients
class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# API 2: Create a new client
class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# API 3: Retrieve client info along with projects
class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer

# API 4: Update a client's info
class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# API 5: Delete a client
class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()

# API 6: Create a new project and assign users
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# API 7: List all projects assigned to the logged-in user
class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

# API 8: Delete a project
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
