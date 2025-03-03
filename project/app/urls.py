from rest_framework import routers
from .views import *


# router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'Employee', EmployeeViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'Admin', AdminViewSet)
router.register(r'Cart1', Cart1ViewSet)

urlpatterns = router.urls

