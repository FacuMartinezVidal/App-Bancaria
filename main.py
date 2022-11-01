

fecha = date.today()
sucursal = input("Ingrese el nombre de la sucursal:")

# creacion de documento


def typeDocument():
    errortype = r(0, 100)
    if errortype < 80:
        value = r(0, 1)
        if value == 0:
            type = '011'
        else:
            type = '099'
        return type
    if errortype > 80:
        invaliddoc = r(12, 98)
        strinvalid = "0"+str(invaliddoc)
        type = strinvalid
        return type


# creacion de nombres aleaotorios
def randomName():
    blankname = r(0, 100)
    if blankname < 80:
        value = r(0, 1)
        if value == 1:
            sex = 'male'
        else:
            sex = 'female'

        name = names.get_full_name(gender=sex)
    else:
        name = ""
    return name


# seleccion de tipo de operacion realizada por cada cliente
def typeOperation():

    value = r(1, 43)
    if value >= 1 and value <= 37:
        if len(str(value)) == 2:
            operation = '0000' + str(value)
        else:
            operation = '00000' + str(value)

    else:
        operation = "0000" + str(value)
    return operation


# creacion de documento de acuerdo el tipo de documento que tengas
def randomDocument(valueTypeDocument):
    error = r(0, 100)
    if error < 85:
        unSexDocument = str(r(12000000, 44000000))
        if valueTypeDocument == '011':
            secondValue = r(0, 1)
            if secondValue == 0:
                thirdValue = r(0, 1)
                if thirdValue == 0:
                    secondType = '30'
                    document = valueTypeDocument+secondType+unSexDocument
                    return document
                else:
                    secondType = '20'
                    document = valueTypeDocument+secondType+unSexDocument
                    return document
            elif secondValue == 1:
                thirdValue = r(0, 1)
                if thirdValue == 0:
                    secondType = '33'
                    document = valueTypeDocument+secondType+unSexDocument
                    return document
                else:
                    secondType = '27'
                    document = valueTypeDocument+secondType+unSexDocument
                    return document
        else:
            document = valueTypeDocument+unSexDocument
            return document
    else:
        document = 0
        return document


# seleccion del codigo de garantia aleatorio que tendra el prestamo
def randomGuaranteeCode():
    guaranteeCode = r(0, 37)
    return guaranteeCode


# asigo el tipo de garantia de acuerdo al codigo de garantia ya establecido
def typeGuarantee(guaranteeCode):
    if guaranteeCode < 33:
        if guaranteeCode == 0:
            typeValueGuarantee = 0
        elif guaranteeCode == 1 or guaranteeCode == 2 or guaranteeCode == 3 or guaranteeCode == 4 or guaranteeCode == 5 or guaranteeCode == 6 or guaranteeCode == 7 or guaranteeCode == 8 or guaranteeCode == 9 or guaranteeCode == 10 or guaranteeCode == 11 or guaranteeCode == 25 or guaranteeCode == 31:
            typeValueGuarantee = 2
        else:
            typeValueGuarantee = 1

    else:
        typeValueGuarantee = r(3, 10)
    return typeValueGuarantee

# seleccion del codigo de moneda


def randomCurrencyCode():
    currencyCode = r(0, 3)
    return currencyCode

# seleccion aleatoria de tipo de Cartera


def randomTypeWallet():
    typeWallet = r(1, 3)
    return typeWallet


# creacion de capital de operacion de acuerdo al tipo de cartera del cliente y la moneda
def randomOperationCapital(typeWallet, currencyCode):
    docazar = r(0, 100)
    if docazar < 95:
        if typeWallet == 1:
            operationCapital = r(50000, 30000000)
            if currencyCode == 0:
                return operationCapital
            elif currencyCode == 1:
                return operationCapital//300

        elif typeWallet == 2:
            operationCapital = r(100000000, 500000000)
            if currencyCode == 0:
                return operationCapital
            elif currencyCode == 1:
                return operationCapital//300

        elif typeWallet == 3:
            operationCapital = r(30000000, 100000000)
            if currencyCode == 0:
                return operationCapital
            elif currencyCode == 1:
                return operationCapital//300
    else:
        operationCapital = r(1, 100)
    return operationCapital

# asignacion de numero de operacion


def operationNumber(operation):
    operationModify = operation[((len(operation))-2):(len(operation))]
    if operationModify == '01':
        opNumber = '131709'
    elif operationModify == '02':
        opNumber = '13712'
    elif operationModify == '03':
        opNumber = '13712'
    elif operationModify == '04':
        opNumber = '131718'
    elif operationModify == '05' or operationModify == '21':
        opNumber = '131708'
    elif operationModify == '06':
        opNumber = '131711'
    elif operationModify == '07':
        opNumber = '131713'
    elif operationModify == '08':
        opNumber = '131714'
    elif operationModify == '09':
        opNumber = '131731'
    elif operationModify == '10' or operationModify == '11' or operationModify == '12' or operationModify == '13' or operationModify == '14' or operationModify == '15' or operationModify == '16' or operationModify == '17':
        opNumber = '131742'
    elif operationModify == '18':
        opNumber = '131741'
    elif operationModify == '19':
        opNumber = '131738'
    elif operationModify == '20':
        opNumber = '131736'
    elif operationModify == '22':
        opNumber = '132735'
    elif operationModify == '23':
        opNumber = '721731'
    elif operationModify == '24':
        opNumber = '141701'
    elif operationModify == '25':
        opNumber = '150720'
    elif operationModify == '26':
        opNumber = '171131'
    elif operationModify == '27':
        opNumber = '131101'
    elif operationModify == '28':
        opNumber = '721735'
    elif operationModify == '30':
        opNumber = '131728'
    elif operationModify == '31':
        opNumber = '135799'
    elif operationModify == '32':
        opNumber = '161003'
    elif operationModify == '33':
        opNumber = '131744'
    elif operationModify == '34':
        opNumber = '131752'
    elif operationModify == '35':
        opNumber = '131748'
    elif operationModify == '36':
        opNumber = '131792'
    else:
        opNumber = '131792'
    return opNumber


# asignacion de situacion de deudor de acuerdo al atraso
def debtorAssignment():
    debt = r(0, 500)
    if debt >= 0 and debt <= 30:
        debtSituation = 1
    elif debt >= 31 and debt <= 90:
        debtSituation = 2
    elif debt >= 90 and debt <= 180:
        debtSituation = 3
    elif debt >= 181 and debt <= 360:
        debtSituation = 4
    elif debt >= 361 and debt <= 460:
        debtSituation = 5
    else:
        debtSituation = r(6, 10)
    return debtSituation

# asignacion de interes a cobrar de acuerdo al capital


def interestCharge(typeWallet, operationCapital):
    if typeWallet == 1:
        interest = round(operationCapital*0.1)
    elif typeWallet == 2:
        interest = round(operationCapital*0.2)
    elif typeWallet == 3:
        interest = round(operationCapital*0.25)
    elif typeWallet == 4:
        interest = round(operationCapital*0.3)
    else:
        interest = round(operationCapital*0.35)
    return interest


# creacion del dataframe
keys = ['tipoDocumento', 'documento', 'nombreCompleto', 'operacion', 'codigoGarantia', 'tipoGarantia',
        'codigoMoneda', 'capitalOperacion', 'interesCobrar', 'clasificacionDeudor', 'numeroOperacion', 'tipoCartera']
dataframe = []
clients = 30
for x in range(clients):
    # creacion de diccionario con valores independientes
    dictionary = {'tipoDocumento': typeDocument(), 'documento': 0, 'nombreCompleto': randomName(), 'operacion': typeOperation(), 'codigoGarantia': randomGuaranteeCode(), 'capitalOperacion': 0,
                  'interesCobrar': 0, 'tipoGarantia': 0, 'codigoMoneda': randomCurrencyCode(), 'clasificacionDeudor': debtorAssignment(), 'numeroOperacion': 0, 'tipoCartera': randomTypeWallet()}
    # asignando valores dependientes de los diccionarios
    dictionary['documento'] = randomDocument(dictionary['tipoDocumento'])
    dictionary['tipoGarantia'] = typeGuarantee(dictionary['codigoGarantia'])
    dictionary['capitalOperacion'] = randomOperationCapital(
        dictionary['tipoCartera'], dictionary['codigoMoneda'])
    dictionary['interesCobrar'] = interestCharge(
        dictionary['tipoCartera'], dictionary['capitalOperacion'])
    dictionary['numeroOperacion'] = operationNumber(dictionary['operacion'])
    # los coloco en el dataframe
    dataframe.append(dictionary)
    dictionary = {}

# creacion de la base de datos
print(dataframe)
database = pd.DataFrame(dataframe)
print(database)

# creacion del archivo excel
database.to_excel('database.xlsx')

# Suma intereses a cobrar
h = 0
sumaintereses = 0
for h in range(len(database)):
    sumaintereses = sumaintereses+database.iloc[h]['interesCobrar']
    h+1


k = 0
sumacapital = 0
for k in range(len(database)):
    sumacapital = sumacapital+database.iloc[k]['capitalOperacion']
    k+1

errores = []

# errortipodocumento
j = 0
errortipodocumento = 0
capitalerrortipodoc = 0
for j in range(len(database)):
    if database.iloc[j]['tipoDocumento'] != '011' and database.iloc[j]['tipoDocumento'] != '099':
        errortipodocumento = errortipodocumento+1
        if j not in errores:
            capitalerrortipodoc = capitalerrortipodoc + \
                database.iloc[j]['capitalOperacion']
            errores.append(j)
    j+1

# errordocumentoenblanco
i = 0
capitalerrordocumento = 0
errordocumento = 0
for i in range(len(database)):
    if database.iloc[i]['documento'] == 0:
        errordocumento = errordocumento+1
        if i not in errores:
            capitalerrordocumento = capitalerrordocumento + \
                database.iloc[i]['capitalOperacion']
            errores.append(i)
    i+1

# error nombre en blanco
a = 0
errornombre = 0
capitalerrornombre = 0
for a in range(len(database)):
    if database.iloc[a]['nombreCompleto'] == "":
        errornombre = errornombre+1
        if a not in errores:
            capitalerrornombre = capitalerrornombre + \
                database.iloc[a]['capitalOperacion']
            errores.append(a)
    a+1

# error operacion
b = 0
erroroperacion = 0
capitalerroroperacion = 0
for b in range(len(database)):
    if database.iloc[b]['operacion'] != '000001' and database.iloc[b]['operacion'] != '000002' and database.iloc[b]['operacion'] != '000003' and database.iloc[b]['operacion'] != '000004' and database.iloc[b]['operacion'] != '000005' and database.iloc[b]['operacion'] != '000006' and database.iloc[b]['operacion'] != '000007' and database.iloc[b]['operacion'] != '000008' and database.iloc[b]['operacion'] != '000009' and database.iloc[b]['operacion'] != '000010' and database.iloc[b]['operacion'] != '000011' and database.iloc[b]['operacion'] != '000012' and database.iloc[b]['operacion'] != '000013' and database.iloc[b]['operacion'] != '000014' and database.iloc[b]['operacion'] != '000015' and database.iloc[b]['operacion'] != '000016' and database.iloc[b]['operacion'] != '000017' and database.iloc[b]['operacion'] != '000018' and database.iloc[b]['operacion'] != '000019' and database.iloc[b]['operacion'] != '000020' and database.iloc[b]['operacion'] != '000021' and database.iloc[b]['operacion'] != '000022' and database.iloc[b]['operacion'] != '000023' and database.iloc[b]['operacion'] != '000024' and database.iloc[b]['operacion'] != '000025' and database.iloc[b]['operacion'] != '000026' and database.iloc[b]['operacion'] != '000027' and database.iloc[b]['operacion'] != '000028' and database.iloc[b]['operacion'] != '000029' and database.iloc[b]['operacion'] != '000030' and database.iloc[b]['operacion'] != '000031' and database.iloc[b]['operacion'] != '000032' and database.iloc[b]['operacion'] != '000033' and database.iloc[b]['operacion'] != '000034' and database.iloc[b]['operacion'] != '000035' and database.iloc[b]['operacion'] != '000036' and database.iloc[b]['operacion'] != '000037':
        erroroperacion = erroroperacion+1
        if b not in errores:
            capitalerroroperacion = capitalerroroperacion + \
                database.iloc[b]['capitalOperacion']
            errores.append(b)
    b+1

# codigo de garantia error
c = 0
errorcodgarantia = 0
caperrorcodgarantia = 0
for c in range(len(database)):
    if database.iloc[c]['codigoGarantia'] > 33:
        errorcodgarantia = errorcodgarantia+1
        if c not in errores:
            caperrorcodgarantia = caperrorcodgarantia + \
                database.iloc[c]['capitalOperacion']
            errores.append(c)
    c+1

# tipo de garantia error
d = 0
errortipogarantia = 0
captipogarantia = 0
for d in range(len(database)):
    if database.iloc[d]['tipoGarantia'] >= 3:
        errortipogarantia = errortipogarantia+1
        if d not in errores:
            captipogarantia = captipogarantia + \
                database.iloc[d]['capitalOperacion']
            errores.append(d)
    d+1

# codigo de moneda no definido
e = 0
errorcodmoneda = 0
caperrorcodmoneda = 0
for e in range(len(database)):
    if database.iloc[e]['codigoMoneda'] > 2:
        errorcodmoneda = errorcodmoneda+1
        if e not in errores:
            caperrorcodmoneda = caperrorcodmoneda + \
                database.iloc[e]['capitalOperacion']
            errores.append(e)
    e+1

# capitaldeoperacion no valido
f = 0
errorcapoperacion = 0
for f in range(len(database)):
    if database.iloc[f]['capitalOperacion'] == 0:
        errorcapoperacion = errorcapoperacion+1
    f+1


# clasificacionDeudor no definida
g = 0
errorclasificaciondedeudor = 0
caperrorcladeudor = 0
for g in range(len(database)):
    if database.iloc[g]['clasificacionDeudor'] > 5:
        errorclasificaciondedeudor = errorclasificaciondedeudor+1
        if g not in errores:
            caperrorcladeudor = caperrorcladeudor + \
                database.iloc[g]['capitalOperacion']
            errores.append(g)
    g+1


data = ["Tipo de documento invalido ", "Numero de documento invalido ", "Nombre en blanco ", "Codigo de operacion",
        "Codigo de garantia", "Tipo de garantia", "Codigo de moneda", "Capital no valido", "Clasificacion de deudor"]
columns = ["Tipo de error", "Cantidad de errores", " ", "  ",
           "   ", "    ", "     ", "      ", "Suma de capital"]


dbs1 = []
dfs1 = pd.DataFrame(dbs1)
dfs1.to_excel('controlerrores.xlsx')

filesheet = "./controlerrores.xlsx"
wb = load_workbook(filesheet)

sheet = wb.active

sheet.merge_cells('A1:L1')
sheet['A1'] = "Control de errores"
sheet['A3'] = "Sucursal"
sheet['A5'] = "Fecha de la cartera"
sheet['A7'] = "Total del capital de las operaciones (INT)"
sheet['A8'] = "Interes devengado a cobrar(INT)"
sheet['A9'] = "Deuda total Cap+Intc(INT)"
sheet['A10'] = "Cantidad de registros del archivo"
sheet['H3'] = sucursal
sheet['H5'] = fecha
sheet['H7'] = str(sumacapital)+"$"
sheet['H8'] = str(sumaintereses)+"$"
sheet['H9'] = str(sumacapital+sumaintereses)+"$"
sheet['H10'] = clients


sheet.merge_cells('A11:L11')
sheet['A11'] = "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
sheet['A12'] = "Tipo de error"
sheet['A14'] = "Tipo de documento invalido-"
sheet['A16'] = "Numero de documento invalido-"
sheet['A18'] = "Nombre en blanco-"
sheet['A20'] = "Codigo de operacion invalido-"
sheet['A22'] = "Codigo de garantia-"
sheet['A24'] = "Tipo de garantia-"
sheet['A26'] = "Codigo de moneda-"
sheet['A28'] = "Capital no valido-"
sheet['A30'] = "Clasificacion de deudor-"
sheet['B12'] = "Cantidad de errores"
sheet['B14'] = errortipodocumento
sheet['B16'] = errordocumento
sheet['B18'] = errornombre
sheet['B20'] = erroroperacion
sheet['B22'] = errorcodgarantia
sheet['B24'] = errortipogarantia
sheet['B26'] = errorcodmoneda
sheet['B28'] = errorcapoperacion
sheet['B30'] = errorclasificaciondedeudor
sheet['H12'] = "Suma capital de errores"
sheet['H14'] = str(capitalerrortipodoc)+"$"
sheet['H16'] = str(capitalerrordocumento)+"$"
sheet['H18'] = str(capitalerrornombre)+"$"
sheet['H20'] = str(capitalerroroperacion)+"$"
sheet['H22'] = str(caperrorcodgarantia)+"$"
sheet['H24'] = str(captipogarantia)+"$"
sheet['H26'] = str(caperrorcodmoneda)+"$"
sheet['H30'] = str(caperrorcladeudor)+"$"

wb.save(filesheet)
