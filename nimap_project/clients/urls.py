from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

# router = DefaultRouter()
# router.register(r'clients', ClientViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('clients/<int:client_id>/projects/', ProjectViewSet.as_view({'post': 'create'})),
# ]

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'clients/(?P<client_id>\d+)/projects', ProjectViewSet, basename='client-projects')

urlpatterns = [
    path('', include(router.urls)),
]
