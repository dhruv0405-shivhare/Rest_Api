from rest_framework import routers
from .views import 
from django.urls import path,include

router = routers.SimpleRouter()
router.register(r'users', StudentViewSet)

urlpatterns = router.urls