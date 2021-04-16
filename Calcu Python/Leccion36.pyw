from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
operacion=""
resultado=0
reset_pantalla=False
Numero=StringVar()
pantalla=Entry(miFrame, textvariable=Numero)
pantalla.grid(row=1,column=1,padx=5,pady=5,columnspan=4)
pantalla.config(background="black", fg="yellow",justify="right")
def Numeropul(num):
	global operacion
	global reset_pantalla
	if reset_pantalla!=False:
		Numero.set(num)
		reset_pantalla=False
	else:	
		Numero.set(Numero.get() + num)
def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	reset_pantalla=True
	resultado+=float(num)
	operacion="suma"
	Numero.set(resultado)
num1=0

contador_resta=0

def resta(num):
	global operacion
	global resultado
	global num1
	global reset_pantalla
	global contador_resta
	if contador_resta==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-float(num)
		else:
			resultado=float(resultado)-float(num)	
		Numero.set(resultado)
		resultado=Numero.get()
	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True
contador_multi=0
def multiplica(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla
	if contador_multi==0:
		num1=float(num)		
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*float(num)
		else:
			resultado=float(resultado)*float(num)	
		Numero.set(resultado)		
		resultado=Numero.get()
	contador_multi=contador_multi+1
	operacion="multiplicacion"
	reset_pantalla=True
contador_divi=0
def divide(num):
	global operacion
	global resultado
	global num1
	global contador_divi
	global reset_pantalla
	if contador_divi==0:
		num1=float(num)		
		resultado=num1
	else:
		if contador_divi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)	
		Numero.set(resultado)		
		resultado=Numero.get()
	contador_divi=contador_divi+1
	operacion="division"
	reset_pantalla=True
def elresultado():
	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi
	if operacion=="suma":
		Numero.set(resultado+float(Numero.get()))
		resultado=0
	elif operacion=="resta":
		Numero.set(float(resultado)-float(Numero.get()))
		resultado=0
		contador_resta=0
	elif operacion=="multiplicacion":
		Numero.set(float(resultado)*float(Numero.get()))
		resultado=0
		contador_multi=0
	elif operacion=="division":
		Numero.set(float(resultado)/float(Numero.get()))
		resultado=0
		contador_divi=0
	resultado=0
def borrar():
	Numero.set("")
#Fila 1
boton7=Button(miFrame,text="7",width=3, command=lambda:Numeropul("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3, command=lambda:Numeropul("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3, command=lambda:Numeropul("9"))
boton9.grid(row=2,column=3)
botonmul=Button(miFrame,text="x",width=3,command=lambda:multiplica(Numero.get()))
botonmul.grid(row=2,column=4)
#Fila 2
boton4=Button(miFrame,text="4",width=3, command=lambda:Numeropul("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3, command=lambda:Numeropul("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3, command=lambda:Numeropul("6"))
boton6.grid(row=3,column=3)
botonrest=Button(miFrame,text="-",width=3,command=lambda:resta(Numero.get()))
botonrest.grid(row=3,column=4)
#Fila 3
boton1=Button(miFrame,text="1",width=3, command=lambda:Numeropul("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3, command=lambda:Numeropul("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3, command=lambda:Numeropul("3"))
boton3.grid(row=4,column=3)
botonmas=Button(miFrame,text="+",width=3, command=lambda:suma(Numero.get()))
botonmas.grid(row=4,column=4)
#Fila 4
boton0=Button(miFrame,text="0",width=3, command=lambda:Numeropul("0"))
boton0.grid(row=5,column=1)
botonp=Button(miFrame,text=".",width=3, command=lambda:Numeropul("."))
botonp.grid(row=5,column=2)
botonig=Button(miFrame,text="=",width=3, command=lambda:elresultado())
botonig.grid(row=5,column=3)
botondiv=Button(miFrame,text="/",width=3, command=lambda:divide(Numero.get()))
botondiv.grid(row=5,column=4)
botonc=Button(miFrame,text="C",width=3, command=lambda:borrar())
botonc.grid(row=6,column=1)
raiz.mainloop()