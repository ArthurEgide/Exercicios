#	Tested on Python 3.7

#   Subprogramas

def ordenar(lista):     #   Ordena a lista em ordem crescente
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    lista.pop(0)        #   Remove o número de cartas
    lista.sort()
    return lista

def lerPrecos():       #   Extrai do arquivo as figurinhas
    listas = []
    try:
        with open("entrada.txt", "r") as arq:
            linha = arq.readline()
            while (linha != ''):
                if len(linha.split()) > 1:      #   Verifica se é uma linha com valores(1°~5°)
                    listas.append(ordenar(linha.split()))
                else:       #   Caso seja a linha com a quantidade de pacotes(6°)
                    numConj = linha.split()[0]
                linha = arq.readline()
        return listas,numConj
    except IOError:
        print('Erro de Entrada ou Saída de dados')

def valor(pcts , numPacotes):
    somaTotal = []

    for b in pcts[0]:       #   Analise de todas as possibilidades
        for f in pcts[1]:
            for l in pcts[2]:
                for v in pcts[3]:
                    for s in pcts[4]:
                        soma = b + f + l + v + s
                        somaTotal.append(soma)
    somaTotal = sorted(somaTotal , reverse = True)
    return somaTotal[:int(numPacotes)]

#   Programa Principal
figs = lerPrecos()[0]       #   Lista com os valores das figurinhas
numPacotes = lerPrecos()[1]     #   Quantidade de pacotes a formar
tops = valor(figs,numPacotes)       #   Soma dos valores de cada um dos melhores pacotes

total = 0
for i in tops:
    total += i

print(total)
