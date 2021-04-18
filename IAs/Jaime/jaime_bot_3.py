import random

class JaimeBot3():

	def __init__(self):
		self.nombre = 'Jaime Bot 3'


	def siguiente_movimiento(self, fila, columna, matriz_juego):
		# Este bot devuelve un número al azar a la izquierda , en el mismo o a la derecha de donde ha puesto el jugador anterior
		return min(7, max(1, columna + random.randint(-1,1) if columna else random.randint(1, 7)))