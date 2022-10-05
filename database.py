
#importaciones
from hashlib import new
import names
import pandas as pd
from random import randint as r

#creacion de nombres aleaotorios
def randomName():
    value=r(0,1)
    if value==1:
        sex='male'
    else:
        sex='female'
    
    name=names.get_full_name(gender=sex)
    return name

#seleccion de tipo de documentos #011=CUIT/CUIL/CDI #099=personas fisicas
def typeDocument(value):
    if value==1:
        type='011'
    else:
        type='099'
    return type

#seleccion de tipo de operacion realizada por cada cliente
def typeOperation():
    value=r(1,37)
    if len(str(value))==2:
        operation='0000' + str(value)
    else:
        operation='00000' + str(value)
    return operation


#creacion estrcutura de base de datos 
dataframe = [{'tipoDocumento':typeDocument(r(0,1)),'documento': r(20000000,50000000),'nombreCompleto': randomName(),
                'operacion': typeOperation(),'codigoGarantia':r(0,33), }]

#creacion de base de datos
# database= pd.DataFrame(dataframe)



def newDataBase(clients,keys):
    dataframe=[]
    columns={x:0 for x in keys}
    for x in range(clients+1):
        dataframe.append(columns)
    return dataframe
clients=200
keys=['tipoDocumento','documento','nombreCompleto','operacion','codigoGarantia','tipoGarantia','codigoMoneda','capitalOperacion','interesCobrar','clasificacionDeudor','fecha1erVencimientoImpago','AtrasoDeuda','NumeroOperacion','cuentaContableCapital','fechaUltimoPago','tipoCartera']

dataframe=newDataBase(clients,keys)
database= pd.DataFrame(dataframe)
print(database)
database.to_excel("baseDatos.xlsx")