

# importo las librerias necesarias para excel
import pandas as pd
import numpy


# defino la ubicacion de mis archivos
basepath = "D:/Desktop/App-Bancaria"

# defino los nombres de las base de datos (provisorio)
database = basepath + "/ejemplo.xlsx"

# defino las tablas
# en sheet_name se pone la hoja que queres usar
dataframe = pd.read_excel(database, sheet_name="Sheet1")

# .head() nos permite visualizar las primeras 5 de filas de nuestros datos
# .tail() nos permite visualizar las ultimas 5 filas de nuestros datos
# .describe() nos da algunas caracteristicas de nuestros datos
# .dropna() filtrado de datos (ej. sacos los datos con valor NaN)
# .fillna() dentro del parentis colocas el valor con el que queres que se rellenen las datos con valor NaN
# dataframe['nombres'] solo me trae la columna mencionada en los corchetes
# .loc[] obtengo solo los datos de la fila 0, y si pongo [0:3] obtengo desde la 1 a la 2, [1,2,3] obtengo las que quiero
# database[database['documento'] < 44000000] es un condicional donde obtengo todos los documentos (en este caso) mayor a
# a 44000000, para usar "and" como condicional lo debo susplantar por "&"
# databas[database[nombre].str.contains()] me busca todos los string los cuales contengan lo que ponga en el parentesis
# database["nueva columna"]=valor para crear nuevas columnas, .apply() para ponerme una funcion que me ayude a crearla
# tambien si yo quiero axis=1 le aplicara la funcion o operacion a cada fila de nuestra base de datos
# database.groupby('nombres') me agrupa las filas que tengas en el mismo valor dentro de las columnas
# database.groupby(columna).agg({
#    'columna2': 'sum', #con sum me suma todos los valores de la columna 2
#    'columna3': 'mean', #me hace un promedio de los valores de la columna 3
#    'columna4: 'max', #me obtiene el maximo valor de la columna 4
# })
# .to_xlsx () para guardar una nueva base de datos, y dentro del parentesis el nombre del nuevo archivo
# pd.DataFrame(diccionario) creo una nueva base de datos a traves de diccionarios, donde la key es la columna y
# value el valor que queres cargar en la columna

