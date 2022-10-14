import pandas as pd
from openpyxl import load_workbook
from database import clients

excel=load_workbook('database.xlsx', data_only=True)
sheet_excel= excel.active

dic={}
capital_operacion= sheet_excel['G2' : 'G7']
clasificacionDeudor= sheet_excel['K2' : 'K7']
tipoGarantia= sheet_excel['I2' : 'I7']
tipoCartera= sheet_excel['M2' : 'M7']
lst_capitalOperacion=[]
for fila in capital_operacion:
    for celda in fila:
        lst_capitalOperacion.append(celda.value)

lst_clasificacionDeudor=[]
for fila in clasificacionDeudor:
    for celda in fila:
        lst_clasificacionDeudor.append(celda.value)

lst_tipoGarantia=[]
for fila in tipoGarantia:
    for celda in fila:
        lst_tipoGarantia.append(celda.value)

lst_tipoCartera=[]
for fila in tipoCartera:
    for celda in fila:
        lst_tipoCartera.append(celda.value)
        


lst_dicAux=[]
for x in range (clients):
    lst_dicAux.append({'tipoCartera':0,'situacionDeudor':0,'tipoGarantia':0, 'capital':0})

aux=0
aux2=0
aux3=0
aux4=0
for dic in lst_dicAux:
    for keys in dic:
        if keys=='tipoCartera':
            dic[keys]=lst_tipoCartera[aux]
            aux+=1
        if keys=='situacionDeudor':
            dic[keys]=lst_clasificacionDeudor[aux2]
            aux2+=1
        if keys=='tipoGarantia':
            dic[keys]=lst_tipoGarantia[aux3]
            aux3+=1
        if keys=='capital':
            dic[keys]=lst_capitalOperacion[aux4]
            aux4+=1

lst_carteraConsumo=[]
for dic in lst_dicAux:
    for keys in dic:
        if keys=='tipoCartera':
            if dic['tipoCartera']==1:
                lst_carteraConsumo.append(dic)

lst_deudor1=[]
lst_deudor2=[]
lst_deudor3=[]
lst_deudor4=[]
lst_deudor5=[]

for dic in lst_carteraConsumo:
    for keys in dic:
        if keys=='situacionDeudor':
            if dic['situacionDeudor']==4:
                print(dic['situacionDeudor'])
                lst_deudor2.append(dic)
                
