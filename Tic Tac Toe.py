import time
import random
import os
def inicio_juego():
	print("Bienvenido...")
	time.sleep(1)
	while True:
		ficha = input("Selecciona ficha X / O\n")
		ficha = ficha.upper()
		if ficha == "X":
			humano = "X"
			ordenador = "O"
			break
		elif ficha == "O":
			humano = "O"
			ordenador = "X"
			break
		else:
			print("Por favor escoja alguna de las 2 fichas")
	return(humano,ordenador)
#Creacion del tablero
def tablero():
	print("TIC TAC TOE")
	print("		 |		    |	         ")
	print("1 {}      |2 {}       |3  {}		   ".format(matriz[0],matriz[1],matriz[2]))
	print("		 |		    |		     ")
	print("------------------------------")
	print("		 |		    |		     ")
	print("4 {}      |5 {}       |6  {}		   ".format(matriz[3],matriz[4],matriz[5]))
	print("		 |		    |		     ")
	print("------------------------------")
	print("		 |		    |		     ")
	print("7 {}      |8 {}       |9  {}		   ".format(matriz[6],matriz[7],matriz[8]))
	print("		 |		    |		     ")
#Finales
def empate(matriz):
	empate=True
	i=0
	while(empate==True and i<9):
		if matriz[i] == " ":
			empate=False
		i=i+1		
	return empate

def victoria(matriz):
	if (matriz[0]==matriz[1]==matriz[2]!=" "or matriz[3]==matriz[4]==matriz[5]!=" "or matriz[6]==matriz[7]==matriz[8]!=" "
		or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or
		matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
		return True
	else:
		return False
#Movimientos
def movimientos_jugador():
	while True:
		posiciones=[0,1,2,3,4,5,6,7,8,9]
		casilla=int(input("Seleccione una casilla: "))
		if casilla not in posiciones:
			print("Casilla no disponible")
		else:
			if matriz[casilla-1]==" ":
				matriz[casilla-1]=humano
				break
			else:
				print("Casilla no disponible")
def movimiento_maquina():
	posiciones=[0,1,2,3,4,5,6,7,8,9]
	casilla = 9
	parar = False
	for i in posiciones:
		copia=list(matriz)
		if copia[i]==" ":
			copia[i]=ordenador
			if victoria(copia)==True:
				casilla=i
	if casilla==9:
		for iteracion in posiciones:
			if copia [iteracion]==" ":
				copia[iteracion]=humano
				if victoria(copia)==True:
					casilla=iteracion
	if casilla==9:
		while(not parar):
			casilla=random.randint(0,9)
			if matriz[casilla]==" ":
				parar=True
	matriz[casilla]=ordenador
while True:
	matriz=[" "]*10
	os.system("cls")
	humano,ordenador=inicio_juego()
	partida=True
	ganador=0
	while partida:
		ganador=ganador+1
		os.system("cls")
		tablero()
		if victoria(matriz):
			if ganador%2==0:
				print("Gano el jugador")
				print("\nFin del juego")
				print("\nReiniciando")
				time.sleep(5)
				partida=False
			else:
				print("Gano el ordenador")
				print("\nFin del juego")
				print("\nReiniciando")
				time.sleep(5)
				partida=False
		elif empate(matriz):
			print("Empate")
			print("\nFin del juego")
			print("\nReiniciando")
			time.sleep(5)
			partida=False
		elif ganador%2==0:
			print("El ordenador esta pensando")
			time.sleep(2)
			movimiento_maquina()
		else:
			movimientos_jugador()