import requests
from bs4 import BeautifulSoup

class Questao_9():

    def __init__(self):
        """ Constructor. """
        self.request = requests.get(
            "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html")
        self.states = ['df', 'mt', 'go', 'ms']
        self.data = ''
        self.usr_choice = ''

    def init_class(self):

        self.request.encoding = self.request.apparent_encoding
        bs = BeautifulSoup(self.request.text, "lxml")
        self.table = bs.html.body.find('div', {"class": "tabela"})
        self.lines = bs.html.body.article.find_all('div', {'class': 'linha'})

    def proc_data(self):

        self.init_class()
        finish = False
        while not finish:
            self.data = input("Digite a sigla de um estado do Centro Oeste: ")
            for line in self.lines:
                _state = line.find_all("div", {"class": "celula"})[0].text
                if self.data == _state.lower():
                    self.usr_choice = line.text
                    finish = True

    def vis_print(self):

        print("Questão 9".center(75), sep='\n')
        self.init_class()
        print('Conteúdo da tabela:\n {} '.format(self.table.get_text()), sep='\n')
        self.proc_data()
        print("{}".format(self.usr_choice),''.rjust(75), sep="\n")


Questao_9().vis_print()