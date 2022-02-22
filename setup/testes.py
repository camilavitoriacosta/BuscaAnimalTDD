from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    ## etapas para ser executadas antes de iniciar os testes
    def setUp(self):
        # configurar para utilizar o Google como navegador principal
        self.browser = webdriver.Chrome(r'C:\Users\vivim\Desktop\Projetos\TDD_buscaAnimal\chromedriver.exe')

    ## etapas que ocorrem após todos os testes
    def tearDown(self):
        self.browser.quit() ## fecha o browser

    def test_abre_janela_do_chrome(self):
        ''' Teste para abrir a janela do servidor '''
        self.browser.get(self.live_server_url) #vai para o endereço

    def test_deu_ruim(self):
        '''Teste de exemplo que irá falhar'''
        self.fail("deu ruim")