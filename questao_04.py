from validation import Validate

class Questao_4():

    def __init__(self):

        self.input = []
        self.list = []

    def init_class(self):

        while len(self.input) < 5:
            self.input.append(Validate().validate_values(
                "Informe um numero: ", zero=True))

    def proc_data(self):

        self.init_class()
        self.list = self.input.copy()
        self.list.reverse()

    def vis_print(self):

        print("Questão 4".center(75), sep='\n')
        self.proc_data()
        print("{0}O resultado da ordem inversa do vetor {1} é de: {2}.".format(
        self.input, self.list),''.rjust(75), sep="\n")

Questao_4().vis_print()