from django.urls import include, path
from rest_framework import routers
from .views import FolderViewSet, DocumentViewSet, WorkLogViewSet, WorkViewSet
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'folders', FolderViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'work', WorkViewSet)
router.register(r'worklogs', WorkLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()