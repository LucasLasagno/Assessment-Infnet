from validation import Validate

class Questao_2():

    def __init__(self):

        self.input = 0
        self.data = []
        self.numero = 0

    def init_class(self):

        self.input = Validate().validate_values("Informe um numero: ")

    def process_data(self):

        self.init_class()

        for i in range(1, (self.input + 1)):
            if i % 2 == 0:
                self.data.append(i)
            else:
                pass
        self.numero = sum(self.data)

    def vis_print(self):

        print('Questao 2'.center(75), sep='\n')
        self.process_data()
        print("O resultado da soma dos numeros pares de 1 a {} é de: {}".format(
                self.input, self.num),''.rjust(75), sep="\n")

Questao_2().vis_print()