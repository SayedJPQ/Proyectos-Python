import sys
import socket
objetivo = socket.gethostbyname(input("Inserte direccion ip: "))
print("Escaneando el objetivo: " + objetivo)
try:
#Rango de puertos
	for port in range (1,20000):
		iteracion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		resultado = iteracion.connect_ex((objetivo, port))
		if resultado == 0:
			print("El puerto {} esta abierto".format(port))
		resultado.close()
except:
	print("\nSaliendo...")
	sys.exit(0)