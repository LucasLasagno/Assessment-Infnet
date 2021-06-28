def montante(inicial,rendimento,aporte,periodos, eixo_x, eixo_y):
    for n in range(1,periodos+1):
        novo_valor = round((inicial+(rendimento*inicial)/100) + aporte)
        inicial = novo_valor
        eixo_x.append(novo_valor)
        eixo_y.append(n)
        print(f"\nApós {n} períodos, o montante será de R${round(novo_valor)}.")


import matplotlib.pyplot as plt
from Questao_4 import montante
def grafico(eixo_x,eixo_y):
    x = eixo_x
    y = eixo_y
    plt.plot(x, y)
    plt.show()
    exit()


#Programa Principal

inicial = float(input("Informe o valor inicial: "))
rendimento = float(input("Informe o rendimento (%): "))
aporte = float(input("Informe o aporte a cada período: R$"))
periodos = int(input("Informe o total de períodos: "))
eixo_x = []
eixo_y = []
montante(inicial, rendimento,aporte, periodos, eixo_x, eixo_y)
grafico(eixo_x, eixo_y)