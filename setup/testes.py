from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    ## etapas para ser executadas antes de iniciar os testes
    def setUp(self):
        # configurar para utilizar o Google como navegador principal
        self.browser = webdriver.Chrome(r'C:\Users\vivim\Desktop\Projetos\TDD_buscaAnimal\chromedriver.exe')

    ## etapas que ocorrem após todos os testes
    def tearDown(self):
        self.browser.quit() ## fecha o browser

    def test_buscando_um_novo_animal(self):
        '''Teste se um usuario encontra um animal pesquisando'''
        home_page = self.browser.get(self.live_server_url + '/') #vai para o endereço
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
    
    # def test_abre_janela_do_chrome(self):
    #     ''' Teste para abrir a janela do servidor '''
    #     self.browser.get(self.live_server_url) #vai para o endereço

    # def test_deu_ruim(self):
    #     '''Teste de exemplo que irá falhar'''
    #     self.fail("deu ruim")