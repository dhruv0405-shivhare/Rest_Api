from rest_framework import routers
from .views import StudentViewSet
from .views import EmployeeViewSet
from .views import CartViewSet
from .views import AdminViewSet
from .views import Cart1ViewSet
# from django.urls import path,include

router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)
router.register(r'Employee', EmployeeViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'Admin', AdminViewSet)
router.register(r'Cart1', Cart1ViewSet)


urlpatterns = router.urls