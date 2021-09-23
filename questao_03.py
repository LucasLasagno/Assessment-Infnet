from validation import Validate

class Questao_3():
 
    def __init__(self):
        
        self.power = 0
        self.components = {"Informe a base: ": 0, "Informe o expoente: ": 0}

    def init_class(self):
        
        for k in self.components.keys():
            self.components[k] = Validate().validate_values(k)

    def proc_data(self):
        
        self.init_class()
        self.power = self.components["Informe a base: "]**self.components["Informe o expoente: "]

    def vis_print(self):

        print("Questão 03".center(75), sep='\n')
        self.proc_data()
        print("O resultado da potencia de {0} elevado a {1} é de: {2}!".format(
                self.components["Informe a base: "], self.components["Informe o expoente: "], self.power),
            ''.rjust(75), sep="\n")

Questao_3().vis_print()