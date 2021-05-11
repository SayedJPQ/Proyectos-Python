import hashlib

encontrada = 0
input_hash = input("Inserte la contraseña hasheada: ")
pass_doc = input("Inserte el diccionario: ")
try:
	pass_file = open(pass_doc, 'r')
except:
	print("Error:" + pass_doc + "no ha sido encontrada")
for palabra in pass_file:
	palabracifrada = palabra.encode('utf-8')
	palabrahasheada = haslib.md5(palabracifrada.strip())
	digest = palabrahasheada.hexdigest()
	if digest == input_hash:
		print("Contraseña encontrada \n La contraseña es:" + palabra)
		encontrada = 1
		break
if not encontrada:
	print("Contraseña no encontrada" + pass_doc)