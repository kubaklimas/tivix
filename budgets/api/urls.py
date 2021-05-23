from django.urls import path,include
from budgets.api.views import BudgetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('budget', BudgetViewSet)



urlpatterns = [
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]