from django.test import TestCase
from django.core.files import File

from backend.models import Parameter
from backend.models import Image


class ImageModelTest(TestCase):

    def test_image_model_save_and_retrive(self):
        image1 = Image(
            title='image1',
            image=File(open('test_images/image1.jpeg', 'rb'))
        )
        image1.save()

        image2 = Image(
            title='image2',
            image=File(open('test_images/image2.jpeg', 'rb'))
        )
        image2.save()

        all_images = Image.objects.all()
        self.assertEqual(len(all_images), 2)
        self.assertEqual(
            all_images[0].title, image1.title
        )
        self.assertEqual(
            all_images[1].title, image2.title
        )


class ParameterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Parameter.objects.create(id=30, name='Чехлы')

    def test_name_label(self):
        par = Parameter.objects.get(id=30)
        field_label = par._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_name_max_length(self):
        par = Parameter.objects.get(id=30)
        max_length = par._meta.get_field('name').max_length
        self.assertEquals(max_length, 40)

    def test_object_name(self):
        par = Parameter.objects.get(id=30)
        self.assertEquals('Чехлы', str(par))


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

    # def test_login(self):
    #     response = self.client.post(
    #         '/api/v1/user/login',
    #         {
    #             "email": "a.iskakov1989@gmail.com",
    #             "password": "qwer1234A"
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)
