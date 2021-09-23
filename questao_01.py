class Questao_1():

    def __init__(self):

        self.data = (14, 8, 39)

    def init_class(self):

        print('Tupla Original: {}'.format(self.data))

    def tup_org(self):
        
        self.init_class()
        _list = list(self.data)
        _list.sort()
        return tuple(_list)

    def vis_print(self):

        print('Questao 1'.center(75), sep='\n')
        print('Tupla Ordem Crescente: {}'.format(self.tup_org()),
              ''.rjust(75), sep="\n")


Questao_1().vis_print()