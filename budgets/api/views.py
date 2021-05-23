from django.db.models import query
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from budgets.models import Budget
from budgets.api.serializers import BudgetSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
