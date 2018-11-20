import math

def coordenadas(arq):		#  Extrair as coordenadas do arquivo
	pontos = []
	linha = arq.readline()

	while linha != '':
		pontos.append(linha.replace('\n',''))
		linha = arq.readline()

	return pontos

def calculo(pontos):		#  Calcula a distâcia entre os pontos
		maxDist = 0
		pntI = pntF = (0,0)

		for a in range(len(pontos)):		#  Para cada ponto
			for b in range(len(pontos)):		#  Para cada ponto
				x1 = float(pontos[a].split()[0])
				y1 = float(pontos[a].split()[1])

				x2 = float(pontos[b].split()[0])
				y2 = float(pontos[b].split()[1])
				dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))		#  Calcular a distancia de um ponto com todos os outros
				if(dist > maxDist):		#  Verifica se é a maior distância
					pntI = (x1,y1)		#  Registra o Ponto Inicial
					pntF = (x2,y2)		#  Registra o Ponto Final
					maxDist = dist		#  Registra a maior distância

				if((a == len(pontos)-1)and(maxDist== 0)):		#  Caso só haja pontos iguais
					pntI = (x1, y1)  # Registra o Ponto Inicial
					pntF = (x2, y2)  # Registra o Ponto Final
					maxDist = dist  # Registra a maior distância

		return pntI,pntF,maxDist


try:
	titulo = input()
	with open(titulo, "r") as arq:
		coord = coordenadas(arq)
		valores = calculo(coord)
		print('Ponto Inicial = ', valores[0])
		print('Ponto Final = ', valores[1])
		print('Distância entre eles = ', valores[2])

except IOError:
	print("Erro ao abrir ou ao manipular arquivo")
