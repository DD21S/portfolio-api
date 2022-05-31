from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet
from projects.views import TagViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls