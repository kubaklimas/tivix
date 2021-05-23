from django.urls import path,include
from users.api.views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('',UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls')),
]