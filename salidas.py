import pandas as pd
from database import clients
'''
0 = sin garantia
1 = garantia B
2 = garantia A
'''

# Abrir archivo para crear la salida


datos = [[], [], []]

open_file = pd.read_excel("database.xlsx")
clasificacion_deudor = open_file.clasificacionDeudor
tipo_garantia = open_file.tipoGarantia

capital_operacion = open_file.capitalOperacion
interes_cobrar = open_file.interesCobrar

suma_interes_capital = round(capital_operacion + interes_cobrar)


def recorrer_datos(clientes):
    for i in range(clientes):
        datos[0].append(clasificacion_deudor[i])
        datos[1].append(tipo_garantia[i])
        datos[2].append(suma_interes_capital[i])


recorrer_datos(clients)
print(datos)

'''
# creo base de datos
salidas_situacion_deudores = pd.DataFrame(datos)

print(salidas_situacion_deudores)

# creacion del archivo excel
salidas_situacion_deudores.to_excel('situacion_deudores.xlsx')

'''
