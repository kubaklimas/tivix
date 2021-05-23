from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from users.models import User
from budgets.models import Budget


class UserAPITestCase(APITestCase):

    USER_LIST_URL = "/users/"
    USER_LIST_REVERSE = "user-list"
    USER_UPDATE_URL = "/users/{id}/"
    USER_UPDATE_REVERSE = "user-detail"

    def setUp(self):
        budget = Budget.objects.create(category="Car",income = 2000, expenses=1800)
        budget.save()
        user = User.objects.create(username="user1", first_name = "John",last_name = "Doe",email="m@m.com")
        user.budgets.add(budget)


    def test_urls_budgets(self):
        self.assertEqual(self.USER_LIST_URL,reverse(self.USER_LIST_REVERSE))
        self.assertEqual(self.USER_UPDATE_URL.format(id=1),reverse(self.USER_UPDATE_REVERSE,kwargs={"pk": 1}))

    
    def test_add_users(self):
        budget = Budget.objects.create(category="Home",income = 2000, expenses=1800)
        
        data = {"username":"user2","password":"secretkey","first_name":"Jane","email":"em@ail.com","budgets":["1","2"]}
        response = self.client.post(
            reverse(self.USER_LIST_REVERSE), data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        #added not existing budget to our user
        data = {"username":"user3","password":"secretkey","first_name":"Jane","email":"e2m@ail.com","budgets":["1","2","3"]}
        response = self.client.post(
            reverse(self.USER_LIST_REVERSE), data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_delete_user(self):
        user = User.objects.first()
        previous = User.objects.count()
        response = self.client.delete(
            reverse(self.USER_UPDATE_REVERSE, kwargs={"pk": user.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), previous-1)
