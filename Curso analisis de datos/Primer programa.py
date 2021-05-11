import pandas as pd
ruta1="C:/Users/PC0/Desktop/titanic train.csv"
dataframe = pd.read_csv(ruta1)
cabecera=["ID","Sobreviviente","Clase","Nombre","Sexo","Edad","Hermanos","Hijos","Ticket","Tarifa","Cabina","Embarcacion","Bote","Altura","Lugar de d estino"]
dataframe.columns = cabecera
dataframe.head()
ruta2 = "C:/Users/PC0/Desktop/Sayed/titanic_train.csv"
dataframe.to_csv(ruta2)