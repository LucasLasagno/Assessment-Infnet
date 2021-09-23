from validation import Validate

class Questao_5():

    def __init__(self):

        self.input = []
        self.list = []
        self.tuple = ()

    def init_class(self):
        
        finish = False
        while not finish:
            _input = input("Informe um número ou digite a palavra fim para sair: ")
            if _input == "fim":
                finish = True
            else:
                self.input.append(int(_input))

    def proc_data(self):

        even_index = []
        self.init_class()
        for i in self.input:
            if i % 2 != 0:
                self.list.append(i)
        for i in self.input:
            if self.input.index(i) % 2 == 0:
                even_index.append(i)
        self.tuple = tuple(even_index)

    def vis_print(self):

        print("Questão 4".center(75), sep='\n')
        self.proc_data()
        print("{0}Lista de numeros ímpares {1}\n{0}Tupla dos numeros nas posições pares: {2}.".format(
                self.list, self.tuple),''.rjust(75), sep="\n")

Questao_5().vis_print()