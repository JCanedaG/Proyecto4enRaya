import random

class JaimeBot2():

	def __init__(self):
		self.nombre = 'Jaime Bot 2'


	def siguiente_movimiento(self, fila, columna, matriz_juego):
		# Este bot devuelve la misma columna que el jugador anterior como única estrategia
		return columna if columna else random.randint(1, 7)