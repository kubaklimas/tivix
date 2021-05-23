from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from budgets.models import Budget


class BudgetAPITestCase(APITestCase):

    BUDGET_LIST_URL = "/api/budget/"
    BUDGET_LIST_REVERSE = "budget-list"
    BUDGET_UPDATE_URL = "/api/budget/{id}/"
    BUDGET_UPDATE_REVERSE = "budget-detail"

    def setUp(self):
        Budget.objects.create(category="Car",income = 2000, expenses=1800)


    def test_urls_budgets(self):
        self.assertEqual(self.BUDGET_LIST_URL,reverse(self.BUDGET_LIST_REVERSE))
        self.assertEqual(self.BUDGET_UPDATE_URL.format(id=1),reverse(self.BUDGET_UPDATE_REVERSE,kwargs={"pk": 1}))


    def test_create_budget(self):
        data = {"category":"Home", "income":10000, "expenses":9202}
        response = self.client.post(reverse(self.BUDGET_LIST_REVERSE), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Budget.objects.count(), 2)

    
    def test_update_budget(self):
        budget = Budget.objects.create(category="Home",income = 2000, expenses=1800)
        response = self.client.patch(
            reverse(self.BUDGET_UPDATE_REVERSE,kwargs={"pk":budget.id}),{"income" : 2100},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch(
            reverse(self.BUDGET_UPDATE_REVERSE,kwargs={"pk":budget.id}),{"income" : -2100},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_budget(self):
        budget = Budget.objects.first()
        previous = Budget.objects.count()
        response = self.client.delete(
            reverse(self.BUDGET_UPDATE_REVERSE, kwargs={"pk": budget.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Budget.objects.count(), previous-1)
