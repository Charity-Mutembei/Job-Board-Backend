from django.urls import include, path
from rest_framework import routers
from .views import FolderViewSet, DocumentViewSet, WorkLogViewSet, WorkViewSet

router = routers.DefaultRouter()
router.register(r'folders', FolderViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'work', WorkViewSet)
router.register(r'worklogs', WorkLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
