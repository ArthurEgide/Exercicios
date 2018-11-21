#   Auxiliary program responsible for writing the binary file

import struct

tarifa = struct.Struct("256s d")

lista = ['Voce 0.05',
        'Dica 0.75',
        'Obrigado 0.30',
        'Tempo 1.40',
        'Tudo 0.01',
        'Abacaxi 0.89',
        'EU 0.34',
        'As 0.01',
        'De 0.02',
        'Novamente 1.34',
        'Caso 0.21']

def escrever(arq,entrada):      #  Escrita de um arquivo binário

    nome = entrada.split()[0].encode('utf-8')
    preco = float(entrada.split()[1])
    bloco = tarifa.pack(nome,preco)
    arq.write(bloco)

try:
    with open('reference.bin', 'w+b') as arq:
        for i in lista:        #  Loop para escrever as taxas no arquivo binário
            escrever(arq,i)
    print('File created and filled with success')


except IOError:
    print("Error with file manipulation or creation")

