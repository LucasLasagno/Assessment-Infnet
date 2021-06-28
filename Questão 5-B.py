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

def solicitar_PIB(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15):
    rotulos, dados = extrair_dados('Planilha.csv')
    indice_2013 = rotulos.index('2013')
    indice_2020 = rotulos.index('2020')
    indice_pais = rotulos.index('País')

    for elemento in dados:
        if elemento[indice_pais] == x1:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB nos EUA é {PIB}%")
        if elemento[indice_pais] == x2:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na China é {PIB}%")
        if elemento[indice_pais] == x3:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB no Japão é {PIB}%")
        if elemento[indice_pais] == x4:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Alemanha é {PIB}%")
        if elemento[indice_pais] == x5:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB no Reino Unido é {PIB}%")
        if elemento[indice_pais] == x6:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na França é {PIB}%")
        if elemento[indice_pais] == x7:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB no Brasil é {PIB}%")
        if elemento[indice_pais] == x8:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Itália é {PIB}%")
        if elemento[indice_pais] == x9:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Índia é {PIB}%")
        if elemento[indice_pais] == x10:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Rússia é {PIB}%")
        if elemento[indice_pais] == x11:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB no Canadá é {PIB}%")
        if elemento[indice_pais] == x12:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Coreia do Sul é {PIB}%")
        if elemento[indice_pais] == x13:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Espanha é {PIB}%")
        if elemento[indice_pais] == x14:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB no México é {PIB}%")
        if elemento[indice_pais] == x15:
            indice2 = float(elemento[indice_2020])
            indice1 = float(elemento[indice_2013])
            PIB = round((indice2/indice1)*100) - 100
            print(f"A variação do PIB na Indonésia é {PIB}%")

solicitar_PIB('EUA','China','Japão','Alemanha','Reino Unido','França','Brasil','Itália','Índia','Rússia','Canadá','Coreia do Sul','Espanha','México','Indonésia')




