 # -*- coding: utf-8 -*-

#Imports
import os
import time

from jaime_bot_1 import JaimeBot1
from jaime_bot_2 import JaimeBot2
from jaime_bot_3 import JaimeBot3
from jaime_bot_pro_1 import JaimeBotPro1
from jaime_bot_pro_2 import JaimeBotPro2


# Definición de funciones

def ultima_altura_ocupada(columna, matriz_juego):
	columna = columna -1
	for i in range(len(matriz_juego)):
		if matriz_juego[i][columna] == 0:
			return i
	
	return None

def ha_ganado(turno, fila, columna ,matriz_juego):
	# Comprobamos todas las posibles formas de ganar

	####
	# Vertical
	####

	contador = 0
	for i in range(len(matriz_juego)):
		if matriz_juego[fila][i] == turno:
			contador += 1
		else:
			contador = 0
		if contador > 3:
			# Ha ganado
			return True

	####
	# Horizontal
	####

	contador = 0
	for i in range(len(matriz_juego)):
		if matriz_juego[i][columna] == turno:
			contador += 1
		else:
			contador = 0
		if contador > 3:
			# Ha ganado
			return True

	####
	# Diagonal
	####

	contador = 0
	for i in range(len(matriz_juego)-abs(fila-columna)):
		
		if (fila >= columna) and (matriz_juego[abs(fila-columna)+i][i] == turno):
				contador += 1
		elif ((fila < columna)) and (matriz_juego[i][abs(fila-columna)+i] == turno):
				contador += 1
		else:
			contador = 0

		if contador > 3:
			# Ha ganado
			return True



#Comienzo del juego

def jugar_partida(bot1, bot2):

	matriz_juego = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

	seguir_partida = True
	turno = 1

	fila_a_rellenar = None
	posicion = None

	while seguir_partida:
		durante_el_turno = True
		contador_intentos = 0

		while durante_el_turno:
			if turno == 1:
				posicion = bot1.siguiente_movimiento(fila_a_rellenar, posicion, matriz_juego)
			else:
				posicion = bot2.siguiente_movimiento(fila_a_rellenar, posicion, matriz_juego)

			if posicion >= 1 and posicion <= 7:
				#Rellenamos ahora la matriz con la nueva columna introducida siempre y cuando sea posible
				fila_a_rellenar = ultima_altura_ocupada(posicion, matriz_juego)

				if fila_a_rellenar != None:
					matriz_juego[fila_a_rellenar][posicion-1] = turno
					if ha_ganado(turno, fila_a_rellenar, posicion-1, matriz_juego):
						return turno

					
					durante_el_turno = False
					turno = 2 - ((turno + 1)%2)

				else:
					#print('¡La columna introducida ya está llena!')
					contador_intentos += 1
					if contador_intentos > 2:
						return 2 - ((turno + 1)%2)


bot1      = JaimeBot1()
bot2      = JaimeBot2()
bot3      = JaimeBot3()
bot_pro_1 = JaimeBotPro1()
bot_pro_2 = JaimeBotPro2()

IA_1 = bot1
IA_2 = bot_pro_2

partidas_ganadas = [0, 0]

for i in range(1000):
	partidas_ganadas[jugar_partida(IA_1, IA_2)-1] += 1

print('%s %d victorias, %s %d victorias'%(IA_1.nombre, partidas_ganadas[0], IA_2.nombre, partidas_ganadas[1]))