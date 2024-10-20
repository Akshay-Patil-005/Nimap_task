
from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()  # Use SerializerMethodField to show username
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

    def get_created_by(self, obj):
        # This method returns the username of the user who created the client
        return obj.created_by.username

    def get_projects(self, obj):
        # Custom method to return the projects related to the client
        return [{'id': project.id, 'name': project.project_name} for project in obj.projects.all()]


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    users = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()  # Use SerializerMethodField to show username

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'users', 'created_at', 'created_by']

    def get_users(self, obj):
        # This method returns a list of users assigned to the project
        return [{'id': user.id, 'name': user.username} for user in obj.users.all()]

    def get_created_by(self, obj):
        # This method returns the username of the user who created the project
        return obj.created_by.username
