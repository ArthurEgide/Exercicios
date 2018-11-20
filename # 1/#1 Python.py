#  Sub Programa

def analisar(seq):      #  Calcula a média e verifica o menor e maior valor
    menor = maior = seq[0]
    total = 0
    for i in seq:       #  Percorrendo cada número da lista
        if(i>maior):        #  Registrando o maior
            maior = i
        if(i<menor):        #  Registrando o menor
            menor = i
        total += i      #  Contando para fazer a média
    media = total/len(seq)
    return [menor,media,maior]

#  Programa Principal

titulo = input()
numeros = []            #  Lista que será preenchida com os números do arquivo


arquivo = open(titulo,"r")
leia = arquivo.readline()

if(leia!=""):           #  Verificando se o arquivo está vazio
    while(leia!=""):            #  Leitura linha a linha
        numeros.append(float(leia))     #  Preenchendo a lista
        leia = arquivo.readline()
    res = analisar(numeros)     #  Analisando a lista gerada
else:
    res = [None,None,None]
arquivo.close()

print("Menor Valor = {}".format(res[0]))
print("Média dos Valores = {}".format(res[1]))
print("Maior Valor = {}".format(res[2]))
