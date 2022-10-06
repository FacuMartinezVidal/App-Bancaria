
#importaciones
from hashlib import new
import names
import pandas as pd
from random import randint as r
from datetime import date



#funcion que crea la base de datos vacia
def newDataBase(clients):
    keys=['tipoDocumento','documento','nombreCompleto','operacion','codigoGarantia','tipoGarantia','codigoMoneda','capitalOperacion','interesCobrar','clasificacionDeudor','numeroOperacion','tipoCartera']
    dataframe=[]
    columns={x:0 for x in keys}
    for x in range(clients):
        dataframe.append(columns)
    return dataframe
clients=5

#creacion de documento
def typeDocument():
    value=r(0,1)
    if value==0:
        type='011'
    else:
        type='099'
    return type

#creacion de nombres aleaotorios
def randomName():
    value=r(0,1)
    if value==1:
        sex='male'
    else:
        sex='female'
    
    name=names.get_full_name(gender=sex)
    return name

#seleccion de tipo de operacion realizada por cada cliente
def typeOperation():
    value=r(1,37)
    if len(str(value))==2:
        operation='0000' + str(value)
    else:
        operation='00000' + str(value)
    return operation

#creacion de documento de acuerdo el tipo de documento que tengas
def randomDocument(valueTypeDocument):
    unSexDocument=str(r(12000000,44000000))
    if valueTypeDocument=='011':
        secondValue=r(0,1)
        if secondValue==0:
            thirdValue=r(0,1)
            if thirdValue==0:
                secondType='30'
                document=valueTypeDocument+secondType+unSexDocument
                return document
            else:
                secondType='20'
                document=valueTypeDocument+secondType+unSexDocument
                return document
        elif secondValue==1:
            thirdValue=r(0,1)
            if thirdValue==0:
                secondType='33'
                document=valueTypeDocument+secondType+unSexDocument
                return document
            else:
                secondType='27'
                document=valueTypeDocument+secondType+unSexDocument
                return document
    else:
        document=valueTypeDocument+unSexDocument
        return document

#seleccion del codigo de garantia aleatorio que tendra el prestamo
def randomGuaranteeCode():
    guaranteeCode=r(0,33)
    return guaranteeCode

#asigo el tipo de garantia de acuerdo al codigo de garantia ya establecido
def typeGuarantee(guaranteeCode):
    if guaranteeCode==0:
        typeValueGuarantee=0
    elif guaranteeCode==1 or guaranteeCode==2 or guaranteeCode==3 or guaranteeCode==4 or guaranteeCode==5 or guaranteeCode==6 or guaranteeCode==7 or guaranteeCode==8 or guaranteeCode==9 or guaranteeCode==10 or guaranteeCode==11 or guaranteeCode==25 or guaranteeCode==31:
        typeValueGuarantee=2
    else:
        typeValueGuarantee=1
    return typeValueGuarantee
#seleccion del codigo de moneda 
def randomCurrencyCode():
    currencyCode=r(0,1)
    return currencyCode

#seleccion aleatoria de tipo de Cartera
def randomTypeWallet():
    typeWallet=r(1,3)
    return typeWallet

#creacion de capital de operacion de acuerdo al tipo de cartera del cliente y la moneda
def randomOperationCapital(typeWallet,currencyCode):
    if typeWallet==1:
        operationCapital=r(50000,30000000)
        if currencyCode==0:
            return operationCapital
        else:
            return operationCapital//300
    elif typeWallet==2:
        operationCapital=r(100000000,500000000)
        if currencyCode==0:
            return operationCapital
        else:
            return operationCapital//300
    else:
        operationCapital=r(30000000,100000000)
        if currencyCode==0:
            return operationCapital
        else:
            return operationCapital//300

#asignacion de numero de operacion
def operationNumber(operation):
        operationModify=operation[((len(operation))-2):(len(operation))]
        if operationModify=='01':
            opNumber='131709'
        elif operationModify=='02':
            opNumber='13712'
        elif operationModify=='03':
            opNumber='13712'
        elif operationModify=='04':
            opNumber='131718'
        elif operationModify=='05' or operationModify=='21':
            opNumber='131708'
        elif operationModify=='06':
            opNumber='131711'
        elif operationModify=='07':
            opNumber='131713'
        elif operationModify=='08':
            opNumber='131714'
        elif operationModify=='09':
            opNumber='131731'  
        elif operationModify=='10' or operationModify=='11' or operationModify=='12' or operationModify=='13' or operationModify=='14' or operationModify=='15' or operationModify=='16' or operationModify=='17':
            opNumber='131742'
        elif operationModify=='18':
            opNumber='131741'
        elif operationModify=='19':
            opNumber='131738'
        elif operationModify=='20':
            opNumber='131736'
        elif operationModify=='22':
            opNumber='132735'
        elif operationModify=='23':
            opNumber='721731'
        elif operationModify=='24':
            opNumber='141701'
        elif operationModify=='25':
            opNumber='150720'
        elif operationModify=='26':
            opNumber='171131'
        elif operationModify=='27':
            opNumber='131101'
        elif operationModify=='28':
            opNumber='721735'
        elif operationModify=='30':
            opNumber='131728'
        elif operationModify=='31':
            opNumber='135799'
        elif operationModify=='32':
            opNumber='161003'
        elif operationModify=='33':
            opNumber='131744'
        elif operationModify=='34':
            opNumber='131752'
        elif operationModify=='35':
            opNumber='131748'
        elif operationModify=='36':
            opNumber= '131792'     
        else:
            opNumber='131792'  
        return opNumber
#asignacion de situacion de deudor de acuerdo al atraso 
def debtorAssignment(debt):
    if debt>=0 and debt<=30:
        debtSituation=1
    elif debt>=31 and debt<=90:
        debtSituation=2
    elif debt>=90 and debt<=180:
        debtSituation=3
    elif debt>=181 and debt<=360:
        debtSituation=4
    else:
        debtSituation=5
    return debtSituation

#asignacion de interes a cobrar de acuerdo al capital
def interestCharge(typeWallet,operationCapital):
    if typeWallet==1:
        interest=round(operationCapital*0.1)
    elif typeWallet==2:
        interest=round(operationCapital*0.2)
    elif typeWallet==3:
        interest=operationCapital*0.25
    elif typeWallet==4:
        interest=round(operationCapital*0.3)
    else:
        interest=round(operationCapital*0.35)
    return interest

#creacion de la base de dato vacia
dataframe=newDataBase(clients)

#Asignacion de valores independientes de la base de datos vacia
for x in range (len(dataframe)):
    for key in dataframe[x]:
        if key=="tipoDocumento":
            dataframe[x]['tipoDocumento']= typeDocument()
        elif key=='nombreCompleto':
            dataframe[x]['nombreCompleto']= randomName()
        elif key=='operacion':
            dataframe[x]['operacion']= typeOperation()
        elif key=='codigoGarantia':
            dataframe[x]['codigoGarantia']= randomGuaranteeCode()
        elif key=='codigoMoneda':
            dataframe[x]['codigoMoneda']= randomCurrencyCode()
        elif key=='tipoCartera':
            dataframe[x]['tipoCartera']= randomTypeWallet()
        elif key=='clasifacionDeudor':
            dataframe[x]['clasifacionDeudor']= debtorAssignment()
        

#Asignacion de valores dependientes de la base de datos vacia
for x in range (len(dataframe)):
    for key in dataframe[x]:
        if key=='documento':
            dataframe[x]['documento']= randomDocument(dataframe[x]['tipoDocumento'])
        elif key=='tipoGarantia':
            dataframe[x]['tipoGarantia']= typeGuarantee(dataframe[x]['codigoGarantia'])
        elif key=='capitalOperacion':
            dataframe[x]['capitalOperacion']= randomOperationCapital(dataframe[x]['tipoCartera'],dataframe[x]['codigoMoneda'])

#segunda asignacion de valores dependientes
for x in range (len(dataframe)):
    for key in dataframe[x]:
        if key=='interesCobrar':
            dataframe[x]['interesCobrar']= interestCharge(dataframe[x]['tipoCartera'],dataframe[x]['capitalOperacion'])
        elif key=='numeroOperacion':
            dataframe[x]['numeroOperacion']= operationNumber(dataframe[x]['operacion'])

#conviertos la lista de diccionarios en una base de datos
database= pd.DataFrame(dataframe)
print(dataframe)
