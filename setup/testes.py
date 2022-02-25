from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):
    ## etapas para ser executadas antes de iniciar os testes
    def setUp(self):
        # configurar para utilizar o Google como navegador principal
        self.browser = webdriver.Chrome(r'C:\Users\vivim\Desktop\Projetos\TDD_buscaAnimal\chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    ## etapas que ocorrem após todos os testes
    def tearDown(self):
        self.browser.quit() ## fecha o browser

    def test_buscando_um_novo_animal(self):
        '''Teste se um usuario encontra um animal pesquisando'''
        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/') #vai para o endereço
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')
        
        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR,'form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
        
        # Ele desiste de adotar um leão.



    
    
    # def test_abre_janela_do_chrome(self):
    #     ''' Teste para abrir a janela do servidor '''
    #     self.browser.get(self.live_server_url) #vai para o endereço

    # def test_deu_ruim(self):
    #     '''Teste de exemplo que irá falhar'''
    #     self.fail("deu ruim")