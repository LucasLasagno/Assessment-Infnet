import requests
import re
from collections import Counter
from bs4 import BeautifulSoup as bs

class Questao_13():

    def __init__(self):

        self.words = 0
        self.ladies = 0
        self.words_list = []
        self.only_once = []

    def init_class(self):

        self.request = requests.get("http://brasil.pyladies.com/about")
        self.request.encoding = self.request.apparent_encoding
        self.soup = bs(self.request.text, 'lxml')
        for item in self.soup.html.body.article.find_all("div"):
            self.words_list = [re.sub('\W+', '', word).lower()
                               for word in item.text.split()]
        self.words = len(self.words_list)

    def proc_data(self):
        
        self.init_class()
        word_dict = dict(Counter(self.words_list))
        self.ladies = word_dict["ladies"]
        for key, value in word_dict.items():
            if value == 1:
                self.only_once.append(key)

    def vis_print(self):

        print("Questão 10".center(75), sep='\n')
        self.proc_data()
        print("{}Existem {} palavras no conteúdo sobre as PyLadies, das quais\n {} aparecem uma única vez, enquanto que a palavra ladies é\n repetida {} vezes.\n".format(
                  ' ', self.words, len(self.only_once), self.ladies),
              "{}Lista de palavras que ocorrem uma única vez no conteúdo:".format(' '), sep="\n")
        for word in self.only_once:
            print(word)

        print(''.rjust(75), sep="\n")

Questao_10().vis_print()