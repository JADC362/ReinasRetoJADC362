from random import randint

MatrizReinas = [] #Matriz final para la disposición de las reinas en el tablero.
VectoresReinas = [] #Vectores posición [h,k] con las posiciones de la reina respecto a la primera reina de todas.

CASILLA_VACIA = 0 #Constante que representa una casilla vacia.
CASILLA_LLENA = 1 #Constante que representa la posición de una reina.
CASILLA_DENEGADA = 2 #Constante que representa la imposibilidad de que una reina este en esta casilla.

def inicio(tamanoTablero = 8):
	"""Función principal que inicia el programa, inicializando las matrices MatrizReinas y VectoresReinas.

	tamanoTablero: Tamaño nxn que tendra el tablero de ajedrez
	cantidadReinas: Cantidad de reinas a poner en el tablero, con la restricción de que cantidadReinas <= tamanoTablero.
	"""
	contador = 0
	while len(VectoresReinas) != tamanoTablero:
		contador += 1
		del MatrizReinas[:]
		del VectoresReinas[:]
		for i in range(tamanoTablero):
			MatrizReinas.append([])
			for j in range(tamanoTablero):
				MatrizReinas[i].append(CASILLA_VACIA)
		generaciónDisposición(tamanoTablero)

	print("Ciclos realizados: "+str(contador))
	desplegarPosicionesReinas()


def generaciónDisposición(tamanoTablero):
	"""Genera una disposicíón de la posición de las reinas en el tablero. 
		
	tamanoTablero: Tamaño nxn que tendra el tablero de ajedrez
	"""
	matrizTransicional = []

	for i in range(tamanoTablero):
		matrizTransicional.append([])
		for j in range(tamanoTablero):
			matrizTransicional[i].append(CASILLA_VACIA)

	for i in range(tamanoTablero):
		posiciónReina = colocarReina_Aleatorio(i,matrizTransicional[0])
		if posiciónReina != None:
			VectoresReinas.append(posiciónReina)
			matrizTransicional = actualizarRestricciones(tamanoTablero,matrizTransicional, posiciónReina)
		

def colocarReina_Aleatorio(filaK,filaCeroMatrizTrancisional):
	"""Genera la posición de una reina para una fila K. En caso de haber casillas vacias se genera una posición aleatoria dentro de estas.
	Si no hay ninguna posible casilla vacia la posición retornada es nula.

	filaK: Número de la fIla k-esima donde se posicionara una reina.
	filaCeroMatrizTranscisional: Primer vector fila de la matriz transicional donde se posicionara la reina.
	"""

	posiciónReina = None
	cantidadPosibleOpciones = 0
	for casilla in filaCeroMatrizTrancisional:
		if casilla == CASILLA_VACIA:
			cantidadPosibleOpciones += 1

	if cantidadPosibleOpciones > 0:
		columnaK = randint(0, cantidadPosibleOpciones-1)
		contandorCasillasVacias = 0
		contandorCasillaDenegadas = 0

		for i in range(len(filaCeroMatrizTrancisional)):

			if filaCeroMatrizTrancisional[i] == CASILLA_VACIA:
				contandorCasillasVacias += 1
			elif filaCeroMatrizTrancisional[i] == CASILLA_DENEGADA:
				contandorCasillaDenegadas += 1

			if (contandorCasillasVacias-1) == columnaK:
				posiciónReina = [filaK, columnaK+contandorCasillaDenegadas]
				break

		

	return posiciónReina

def actualizarRestricciones(tamanoTablero,matrizTransicional, posiciónReina):

	"""Genera las restricciones en el tablero dada posición de la ultima reina puesta.

	matrizTransicional: Matriz de representación de las restricciones.
	posiciónReina: Posición de la ultima reina puesta.
	"""
	for i in range(len(matrizTransicional)):
		for j in range(tamanoTablero):
			if i == 0:
				matrizTransicional[i][j] = CASILLA_DENEGADA

			if j == posiciónReina[1]:
				matrizTransicional[i][j] = CASILLA_DENEGADA

			if i+posiciónReina[1]==j:
				matrizTransicional[i][j] = CASILLA_DENEGADA

			if i==(tamanoTablero-1)-(j+(tamanoTablero-1-posiciónReina[1])):
				matrizTransicional[i][j] = CASILLA_DENEGADA
	return matrizTransicional[1:]

def desplegarPosicionesReinas():

	"""Posiciona todas las reinas en el tablero de la lista VectoresReina"""

	for reina in VectoresReinas:
		MatrizReinas[reina[0]][reina[1]] = CASILLA_LLENA
	
	imprimirMatriz(MatrizReinas)

def imprimirMatriz(matriz):
	"""Imprime un forma de matriz la lista enviada por parametro"""
	for fila in matriz:
		print(fila)

	print()


inicio(8)