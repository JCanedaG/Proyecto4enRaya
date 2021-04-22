import random

class JaimeBot1():

	def __init__(self):
		self.nombre = 'Jaime Bot 1'


	def siguiente_movimiento(self, fila, columna, matriz_juego):
		# Este bot devuelve un número al azar entre 1 y 7 como única estrategia
		return random.randint(1,7)