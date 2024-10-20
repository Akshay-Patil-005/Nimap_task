from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'clients/(?P<client_id>\d+)/projects', ProjectViewSet, basename='client-projects')

urlpatterns = [
    path('', include(router.urls)),
]
