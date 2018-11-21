'''
	The "aux.py" program is responsible for creating the binary file. Run it before you run this file

'''
import struct

tarifa = struct.Struct("256s d")

# subprogramas
def ler(arq):       #  Leitura de um arquivo binário
    bloco = arq.read(tarifa.size)
    campos = tarifa.unpack(bloco)
    return campos[0].decode("utf-8").rstrip(chr(0)), campos[1]

def carta(carta):
    palavras = []
    linha = carta.readline()
    while( linha != ''):
        linha = linha.split()
        for ind, i in enumerate(linha):
            if(i[-1].islower() or i[-1].isupper()):     #   Garantir palavras sem pontuação
                palavras.insert(ind,i)
            else:
                qntPontos = 1
                while not(i[-1-qntPontos].islower() or i[-1-qntPontos].isupper()):      #      Tratar multiplas pontuações. Exemplo:"Ola!!!"
                   qntPontos += 1
                palavras.insert(ind, i[:-qntPontos])
        linha = carta.readline()
    return palavras

def desconto(lista):        #  Limita a 2 taxações por palavra
    for i in range(len(lista)):
        if(lista[i][1]) >= 2:
            lista[i][1] = 2
    return lista

def taxar(referencias,carta):       #  Aplica as taxas
    historico = []

    for i in range(len(referencias)):
        referencias[i] = referencias[i].split()     #  Faz com que cada elemento de referencia se torne um vetor [palavra,preço]

    for palavra in carta:
        for i in range(len(referencias)):
            if palavra.lower() == referencias[i][0].lower():        #   Verificando se a palavra precisa ser taxada

                if(len(historico)>0):   #   Verificando se existe alguma palavra no histórico
                    for q in range(len(historico)):     #   Contando por palavra no histórico
                        if historico[q][0] == palavra.lower():     #   Verificando se a palavra já foi encontrada
                            historico[q][1] += 1     #   Registrando ocorrência da palavra
                            break       #   Para o loop caso encontre

                        if (q == len(historico)-1):       #   Caso NÃO tenha encontrado e seja o último
                            historico.append([palavra, 1])      #   Adicione ao histórico


                else:       #   Caso historico esteja vazio,inclua por primeiro
                    historico.append([palavra,1])
    abate = desconto(historico)

    preco = 0

    for i in range(len(abate)):
        for q in range(len(referencias)):
            if referencias[q][0].lower() == abate[i][0].lower():
                preco += (abate[i][1] * float(referencias[q][1]))

    return preco

def imposto(tarifa):
    try:
        with open('imposto.txt','w') as imposto:
            imposto.write('O imposto cobrado é de R$ {:.2f}'.format(tarifa))
    except IOError:
        print('Erro ao manipular o arquivo')
#  Programa principal

titulo = input()
tributos = []

try:
    with open('referencia.bin', 'rb') as ref:
        pointer = 0
        while(ref.read(1) != b''):
            ref.seek(pointer * tarifa.size)
            palavra, preco = ler(ref)
            tribConc = palavra + ' ' + str(preco)
            tributos.append(tribConc)
            pointer += 1
        with open(titulo, 'r') as mensagem:
            carta = carta(mensagem)
            taxa = taxar(tributos, carta)
            imposto(taxa)


except IOError:
    print("Erro ao abrir ou ao manipular arquivo. Certifique-se de ter utilizado o 'Auxiliar.py' por primeiro.")

