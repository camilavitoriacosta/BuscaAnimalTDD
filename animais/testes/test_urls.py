from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utliza_view_index(self):
        request = self.factory.get('/')
        response = index(request)
        
        self.assertEqual(response.status_code, 200)
