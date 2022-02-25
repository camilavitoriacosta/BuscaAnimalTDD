from urllib.request import Request
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal
class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )
    
    def test_index_view_retorna_caracteristicas_do_animal(self):
        """teste que verifica se a index retorna as características do animal pesquisado"""
        response = self.client.get('/', 
            {'buscar':'Leão'}
        )
        caracteristica_aniaml_pesquisado = response.context['caracteristicas']
        self.assertEqual(caracteristica_aniaml_pesquisado[0].nome_animal, "Leão")
        self.assertIs(type(response.context['caracteristicas']), QuerySet)