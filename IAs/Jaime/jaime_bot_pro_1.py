import random

class JaimeBotPro1():

	def __init__(self):
		self.nombre = 'Jaime Bot Pro 1'


	def siguiente_movimiento(self, fila, columna, matriz_juego):
		huecos_columnas = [matriz_juego[:][j].count(0) for j in range(len(matriz_juego[0]))]

		posibles = [i for i, e in enumerate(huecos_columnas) if e == min(huecos_columnas)]

		return posibles[random.randint(1, len(posibles)) - 1] + 1