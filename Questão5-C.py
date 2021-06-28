import matplotlib.pyplot as plt
def extrair_dados(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r', encoding='utf8')

    conteudo = arquivo.read()

    arquivo.close()
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
    return rotulos, dados

def exibir_grafico(x, y):
  plt.plot(x, y)
  plt.show()

def exibir_grafico_PIB(pais):
  rotulos, dados = extrair_dados('Planilha.csv')
  indice_2013 = rotulos.index('2013')
  indice_2014 = rotulos.index('2014')
  indice_2015 = rotulos.index('2015')
  indice_2016 = rotulos.index('2016')
  indice_2017 = rotulos.index('2017')
  indice_2018 = rotulos.index('2018')
  indice_2019 = rotulos.index('2019')
  indice_2020 = rotulos.index('2020')
  indice_pais = rotulos.index('País')
  anos = [2013,2014,2015,2016,2017,2018,2019,2020]
  PIB = []
  for elemento in dados:
      if elemento[indice_pais] == pais:
          PIB.append(elemento[indice_2013])
          PIB.append(elemento[indice_2014])
          PIB.append(elemento[indice_2015])
          PIB.append(elemento[indice_2016])
          PIB.append(elemento[indice_2017])
          PIB.append(elemento[indice_2018])
          PIB.append(elemento[indice_2019])
          PIB.append(elemento[indice_2020])
  exibir_grafico(anos, PIB)






#Programa Principal
país = str(input("Digite um país:"))
exibir_grafico_PIB(país)
