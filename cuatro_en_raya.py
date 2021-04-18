 # -*- coding: utf-8 -*-

#Imports
import os
import time

from jaime_bot_1 import JaimeBot1


# Definición de funciones

def pintar_tablero(matriz_juego):
  for i in range(len(matriz_juego)): 
    texto_fila = '' 
    for j in range(len(matriz_juego[i])): 
      texto_fila += '|' 
      if matriz_juego[len(matriz_juego)-1-i][j] == 0: 
        texto_fila += ' ' 
      elif matriz_juego[len(matriz_juego)-1-i][j] == 1: 
        texto_fila += 'O' 
      elif matriz_juego[len(matriz_juego)-1-i][j] == 2: 
        texto_fila += 'x' 
      else:
        print('Ups, algo va mal')
    texto_fila += '|'
    print(texto_fila)
    
  print(' - - - - - - -')


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
		"""
		if fila >= columna:
			if matriz_juego[abs(fila-columna)+i][i] == turno:
				contador += 1
			else:
				contador = 0
		else:
			if matriz_juego[i][abs(fila-columna)+i] == turno:
				contador += 1
			else:
				contador = 0
		"""
		if contador > 3:
			# Ha ganado
			return True

#Comienzo del juego

matriz_juego = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

#Comenzamos ahora el juego como tal
jugar = 1#int(input('¿Quieres jugar una partida con alguien? 1+Intro -> Sí, 2+Intro -> No :'))
turno = 1

bot = JaimeBot1()

while jugar == 1:
	durante_el_turno = True
	os.system('clear')
	if turno == 1:
		print('Turno del jugador 1 que juega con los O')
	elif turno == 2:
		print('Turno del jugador 2 que juega con las X')
	else:
		print('Estoy perdido, no sé de quién es el turno: '+str(turno))


	#os.system('clear')
	pintar_tablero(matriz_juego)

	print('\n \n \n')

	#time.sleep(3.0)
	#Definimos inicialmente la variable posición.
	#posicion = 0
	
	while durante_el_turno:
		if turno == 1:
			posicion = int(input('Introduce una posición del 1 al 7:'))
		else:
			posicion = bot.siguiente_movimiento(fila_a_rellenar, posicion, matriz_juego)

		if posicion >= 1 and posicion <= 7:
			#Rellenamos ahora la matriz con la nueva columna introducida siempre y cuando sea posible

			fila_a_rellenar = ultima_altura_ocupada(posicion, matriz_juego)

			if fila_a_rellenar != None:
				matriz_juego[fila_a_rellenar][posicion-1] = turno
				if ha_ganado(turno, fila_a_rellenar, posicion-1, matriz_juego):
					os.system('clear')
					pintar_tablero(matriz_juego)
					jugar = 2
					print('\n\n')
					print('¡Enhorabuena!, ha ganado el jugador '+str(turno))

				
				durante_el_turno = False
				turno = 2 - ((turno + 1)%2)

			else:
				print('¡La columna introducida ya está llena!')

else:
	#os.system('clear')
	print('¡¡¡Gracias por confiar en nuestro software de 4 en raya!!!\n \n \n ESPERAMOS VERTE PRONTO')