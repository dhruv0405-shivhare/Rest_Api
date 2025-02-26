from rest_framework import routers
from .views import StudentViewSet


router = routers.SimpleRouter()
router.register(r'users', StudentViewSet)

urlpatterns = router.urls

