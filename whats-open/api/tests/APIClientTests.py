from rest_framework.test import APITestCase, APITransactionTestCase, APIClient
from django.contrib.auth.models import User # AnonymousUser, 
from os import environ as env
# https://stackoverflow.com/questions/44450533/difference-between-testcase-and-transactiontestcase-classes-in-django-test
# ^APITestCase vs APITransactionTestCase

# https://www.django-rest-framework.org/api-guide/testing/
# ^DRF testing guide

# https://django-testing-docs.readthedocs.io/en/latest/fixtures.html
# ^testing with fixtures

# https://stackoverflow.com/questions/5875111/running-a-specific-test-case-in-django-when-your-app-has-a-tests-directory
# ^running the tests

client = APIClient()
user = User.objects.get(username=env["WOPEN_SUPERUSER"] + env["WOPEN_EMAIL_DOMAIN"])
client.force_authenticate(user=user)


class AlertsTests(APITestCase):
    def test_read(self):
        response = client.get('/api/alerts/')
        assert response.status_code == 200
    
    def test_ordering(self):
        response = client.get('/api/alerts/?ordering=urgency_tag')
        assert response.status_code == 200
    
    def test_search(self):
        response = client.get('/api/alerts/?search=srct&format=json')
        assert response.status_code == 200
    
    def test_filtering(self):
        response = client.get('/api/alerts/?urgency_tag=major&format=json')
        assert response.status_code == 200
    

class CategoriesTests(APITestCase):
    def test_read(self):
        response = client.get('/api/categories/')
        assert response.status_code == 200
    
    def test_ordering(self):
        response = client.get('/api/categories/?ordering=name')
        assert response.status_code == 200
    
    def test_search(self):
        response = client.get('/api/categories/?search=din&format=json')
        assert response.status_code == 200
    
    def test_filtering(self):
        response = client.get('/api/categories/?name=dining&format=json')
        assert response.status_code == 200

class facilitiesTests(APITestCase):
    def test_read(self):
        response = client.get('/api/facilities/')
        assert response.status_code == 200
    
    def test_ordering(self):
        response = client.get('/api/facilities/?ordering=-facility_classifier')
        assert response.status_code == 200
    
    def test_search(self):
        response = client.get('/api/facilities/?search=south&format=json')
        assert response.status_code == 200
    
    def test_filtering(self):
        response = client.get('/api/facilities/?facility_name=Southside')
        assert response.status_code == 200

class LocationsTests(APITestCase):
    def test_read(self):
        response = client.get('/api/locations/')
        assert response.status_code == 200
    
    def test_ordering(self):
        response = client.get('/api/locations/?ordering=-address')
        assert response.status_code == 200
    
    def test_search(self):
        response = client.get('/api/locations/?search=johnson&format=json')
        assert response.status_code == 200
    
    def test_filtering(self):
        response = client.get('/api/locations/?building=Johnson+Center&format=json')
        assert response.status_code == 200

class ScheduleTests(APITestCase):
    def test_read(self):
        response = client.get('/api/schedules/')
        assert response.status_code == 200
    
    def test_ordering(self):
        response = client.get('/api/schedules/?ordering=name')
        assert response.status_code == 200
    
    """Invalid value south?"""
    def test_search(self):
        response = client.get('/api/schedules/?search=Southside+[Fall+%2FSpring+Hours]')
        #print(dir(response))
        assert response.status_code == 200
    
    def test_filtering(self):
        response = client.get('/api/schedules/?name=&valid_start=&valid_end=&twenty_four_hours=true')
        self.assertTrue(response.status_code == 200)
    
    def test_post(self):
        response = client.post('/api/schedules/', {
                                "name": "hi",
                                "valid_start": None,
                                "valid_end": None,
                                "twenty_four_hours": False
                                }, format='json')
        assert response.status_code == 201

# class OpenTimeTests(APITestCase):
#     def test_read(self):
#         response = client.get('/api/categories/')
#         assert response.status_code == 200
    
#     def test_ordering(self):
#         self.assertTrue(True)
    
#     def test_search(self):
#         self.assertTrue(True)
    
#     def test_filtering(self):
#         self.assertTrue(True)
    
#     def test_post(self):
#         client.post('/notes/', {'title': 'new idea'}, format='json')
#         self.assertTrue(True)