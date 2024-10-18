# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import get_object_or_404
# from .models import Client, Project
# from .serializers import ClientSerializer, ProjectSerializer

# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated]
    

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

#     def update(self, request, *args, **kwargs):
#         client = self.get_object()
#         serializer = self.get_serializer(client, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save(updated_at=timezone.now())
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         client = self.get_object()
#         client.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         client = get_object_or_404(Client, id=self.kwargs['client_id'])
#         serializer.save(created_by=self.request.user, client=client)

from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=self.request.now)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if 'client_id' in self.kwargs:
            return Project.objects.filter(client_id=self.kwargs['client_id'])
        return Project.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        client = Client.objects.get(id=self.kwargs['client_id'])
        serializer.save(client=client, created_by=self.request.user)
