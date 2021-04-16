import socket
#Encuentra la ip y nombre del ordenador
nombrehost = socket.gethostname()
ip = socket.gethostbyname(nombrehost)
print("El nombre del ordenador es: " + nombrehost)
print("La ip es: " + ip)