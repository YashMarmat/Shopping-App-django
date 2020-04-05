from django.test import TestCase, Client
from django.urls import reverse
from .models import ShopItem, Offer


class TestUrls(TestCase):

    def test_homepage_url_reference_name(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)

    def test_homepage_url_path(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)

    def test_homepage_uses_correct_template(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')
    
    def test_index_url_reference_name(self):
        request = self.client.get(reverse('index'))
        self.assertEqual(request.status_code, 200)

    def test_index_url_path(self):
        request = self.client.get('/products/')
        self.assertEqual(request.status_code, 200)

    def test_index_uses_correct_template(self):
        request = self.client.get(reverse('index'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'index.html')

class TestModel1(TestCase):

    def setUp(self):
        self.shop = ShopItem.objects.create(
            name  = 'apple',
            price = 1.1,
            stock = 100,
            image_url = 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Carabao_mangoes_%28Philippines%29.jpg'
        )

    def test_model1_content(self):
        self.assertEqual(f'{self.shop.name}', 'apple')
        self.assertEqual(f'{self.shop.price}', '1.1')
        self.assertEqual(f'{self.shop.stock}', '100')
        self.assertEqual(f'{self.shop.image_url}', 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Carabao_mangoes_%28Philippines%29.jpg')


class TestModel2(TestCase):

    def setUp(self):
        self.offer = Offer.objects.create(
            code = '#3454ym',
            description = 'healthy apple',
            discount = '0.5',
        )

    def test_model2_content(self):
        self.assertEqual(f'{self.offer.code}', '#3454ym')
        self.assertEqual(f'{self.offer.description}', 'healthy apple')
        self.assertEqual(f'{self.offer.discount}', '0.5')
        
