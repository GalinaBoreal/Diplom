from django.test import TestCase
from rest_framework.test import APIClient

# client = APIClient()
#
# client.post('/notes/', {'title': 'new idea'}, format='json')


class TestUrls(TestCase):

    def test_shops(self):
        response = self.client.get(
            path='/api/v1/shops'
        )
        self.assertEqual(response.status_code, 200)

    def test_products(self):
        response = self.client.get(
            path='/api/v1/products?shop_id=1&category_id=224',
        )
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        response = self.client.get(
            path='/api/v1/categories',
        )
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(
            '/api/v1/user/login',
            {
                "email": "ivanovaannayuryevna@mail.ru",
                "password": "pas456123"
            }
        )
        self.assertEqual(response.status_code, 200)
