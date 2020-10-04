"""

Proyecto 2. Introduccion al analisis de datos
Autor: Andre Marx Puente Arevalo

"""

"""
CONTENIDO DE LAS LISTAS:

info_movimientos = [id, direccion, origen, destino, anio, fecha, producto, modo_transporte, nombre_compania, valor_total]

"""

#################### Carga de datos ####################

# Importo la libreria que nos permite trabajar con archivos CSVs
import csv

# Inicializo una lista donde guardare los datos
info_movimientos = []

#  Importo los datos a python y los guardo en una lista
with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    # Bucle que guarda los datos
    for linea in lector:
        # El primer elemento son los encabezados
        info_movimientos.append(linea)

# Quito los encabezados
info_movimientos.pop(0)        

#################### Opcion 1. Rutas de importacion y exportacion ####################

# Creo una funcion que regresa las mejores rutas de importacion y exportacion
def mejores_rutas(direccion = "Exports", anios = False, valor = True):
    """

    Parametros
    ----------
    direccion : TYPE, String
        DESCRIPCION. Por defecto es "Exports".
        Puede tomar tambien el valor de "Imports", depende de la direccion
        que se desea ver.
    anios : TYPE, Boolean
        DESCRIPCION. Por defecto es "False", indica que no se queire filtar la
        lista por anios. Si es "True", indica que se quiere filtrar la lista 
        por anios.
    valor : TYPE, Boolean
        DESCRIPCION. Por defecto es "False" y devulve una lista sin considerar
        los valores totales. Si es "True" devulve una lista que considera los
        los valores totales.
        

    Returns
    -------
    Lista que contiene las rutas mas usadas de una cierta direccion,
    temporalidad y el valor.

    """
    
    # Inicializo listas donde guardare los datos
    contados = []
    rutas_demandadas = []
    
    # Verifico que ingresen argumentos validos para direccion
    if direccion in {"Exports", "Imports"}:
        
        # Verifico el argumento de valor
        if valor == False:
     
            # Verifico los argumentos de Temporalidad
            if anios == False:
                
                # Bucle que cuenta las veces que se usaron las rutas
                for movimiento in info_movimientos:
                    contado = [direccion, movimiento[2], movimiento[3]]
                    # Inicializo un contador de usos
                    contador = 0
                    
                    # Verifico si ya conte esta ruta
                    if contado in contados:
                        continue
                    
                    # Cuento las veces que se usa
                    for movimiento_2 in info_movimientos:
                        if contado == [movimiento_2[1], movimiento_2[2], movimiento_2[3]]:
                            contador += 1
                    
                    # Guardo la informacion en la listas
                    contados.append(contado)
                    if contador == 0: 
                        continue
                    rutas_demandadas.append([direccion, movimiento[2], movimiento[3], contador])
                    
                # Ordeno la lista de mayor a menos
                rutas_demandadas.sort(reverse = True, key = lambda flujos: flujos[3])
                    
            elif anios == True:
                
                # Bucle que cuenta las veces que se usaron las rutas
                for movimiento in info_movimientos:
                    contado = [direccion, movimiento[2], movimiento[3], movimiento[4]]
                    # Inicializo un contador de usos
                    contador = 0
                    
                    # Verifico si ya conte esta ruta
                    if contado in contados:
                        continue
                    
                    # Cuento las veces que se usa
                    for movimiento_2 in info_movimientos:
                        if contado == [movimiento_2[1], movimiento_2[2], movimiento_2[3], movimiento_2[4]]:
                            contador += 1
                    
                    # Guardo la informacion en la listas
                    contados.append(contado)
                    if contador == 0: 
                        continue
                    rutas_demandadas.append([direccion, movimiento[2], movimiento[3], movimiento[4], contador])
               
                # Ordeno la lista de mayor a menos
                rutas_demandadas.sort(reverse = True, key = lambda x: (x[3], x[4]))
                    
        elif valor == True:
            
            # Verifico los argumentos de Temporalidad
            if anios == False:
                
                # Bucle que cuenta las veces que se usaron las rutas
                for movimiento in info_movimientos:
                    contado = [direccion, movimiento[2], movimiento[3]]
                    # Inicializo un contador de usos
                    contador = 0
                    # Inicializo el total de valor de los movimientos
                    valor = 0
                    
                    # Verifico si ya conte esta ruta
                    if contado in contados:
                        continue
                    
                    # Cuento las veces que se usa
                    for movimiento_2 in info_movimientos:
                        if contado == [movimiento_2[1], movimiento_2[2], movimiento_2[3]]:
                            contador += 1
                            valor += int(movimiento_2[9])
                    
                    # Guardo la informacion en la listas
                    contados.append(contado)
                    if contador == 0: 
                        continue
                    rutas_demandadas.append([direccion, movimiento[2], movimiento[3], valor, contador])
                    
                # Ordeno la lista de mayor a menos
                rutas_demandadas.sort(reverse = True, key = lambda x: (x[4], x[3]))
                    
            elif anios == True:
                
                # Bucle que cuenta las veces que se usaron las rutas
                for movimiento in info_movimientos:
                    contado = [direccion, movimiento[2], movimiento[3], movimiento[4]]
                    # Inicializo un contador de usos
                    contador = 0
                    # Inicializo el total de valor de los movimientos
                    valor = 0
                    
                    # Verifico si ya conte esta ruta
                    if contado in contados:
                        continue
                    
                    # Cuento las veces que se usa
                    for movimiento_2 in info_movimientos:
                        if contado == [movimiento_2[1], movimiento_2[2], movimiento_2[3], movimiento_2[4]]:
                            contador += 1
                            valor += int(movimiento_2[9])
                    
                    # Guardo la informacion en la listas
                    contados.append(contado)
                    if contador == 0: 
                        continue
                    rutas_demandadas.append([direccion, movimiento[2], movimiento[3], movimiento[4], valor, contador])
                    
                # Ordeno la lista de mayor a menos
                rutas_demandadas.sort(reverse = True, key = lambda x: (x[3], x[5], x[4]))
    
    # Regreso la lista con las rutas
    return rutas_demandadas

# Funcion que calcula la porporcion de crecimiento en el uso de las rutas
def proporcion_rutas(rutas, rutas_anios):
    """

        Parametros
        ----------
        rutas : TYPE, List
            DESCRIPCION. Lista que contiene el total de las veces que se uso una ruta para importar o exportar.
        rutas_anios : TYPE, List
            DESCRIPCION. Lista que contiene el total de las veces que se uso una ruta para importar o exportar por anio.


        Returns
        -------
        Lista que contiene las rutas y su respectiva porporcion de crecimiento durante el ultimo anio.

    """
    # Inicializo la ista que guardara las proprociones por anio
    proporcion_rutas=[]

    # Calculamos la porporcion de usos de las rutas por anios
    for ruta_anio in rutas_anios:
        ruta = [ruta_anio[1], ruta_anio[2]]
        anio = ruta_anio[3]
        proporcion_valor = 0
        porporcion_usos = 0
        for info_ruta in rutas:
            if ruta == [info_ruta[1], info_ruta[2]]:
                proporcion_usos = round(ruta_anio[5] / info_ruta[4], 4)
                proporcion_valor = round(ruta_anio[4] / info_ruta[3], 4)
        # Guardamos las porporciones
        if proporcion_usos == 0:
            continue
        proporcion_rutas.append([ruta_anio[0], ruta_anio[1], ruta_anio[2], anio, proporcion_valor, proporcion_usos])

    # Regreso la lista con la informacion
    return proporcion_rutas


#################### Opcion 2. Medio de transporte utilizado ####################
     
# Fucnion que obtiene los medio de transporte mas utilizados
def medio_transporte(direccion = False):
    """

    Parametros
    ----------
    direccion : TYPE, String
        DESCRIPCION. Por defecto es "False", es decir, no considera ninguna direccion.
        Puede tomar tambien el valor de "Imports" o "Exports", depende de la direccion
        que se desea ver.
        

    Returns
    -------
    Lista que contiene los medios de trasporte mas utilizados, con el numero de veces
    que se ha usado, el valor total de la mercancia que ha movido, dependiendo la
    de la direccion que se desea analizar.

    """
    
    # Inicializo las listas donde se guardara la informacion
    transportes_contados = []
    transportes = []
    
    # Verifico los posibles valores del parametro
    if direccion == False:
        
        # Obtengo por cada medio de transporte cuantas veces se utilizo y el valor
        # que ha llevado
        for movimiento in info_movimientos:
            transporte_contado = movimiento[7]
            contador = 0
            valor = 0
            
            # Verifico que no lo haya contado ya
            if transporte_contado in transportes_contados:
                continue
            
            # Cuento las veces que se uso y el valor que movio
            for movimiento_2 in info_movimientos:
                if transporte_contado == movimiento_2[7]:
                    contador += 1
                    valor += int(movimiento_2[9])
            
            # Guardo la informacion en listas
            transportes_contados.append(transporte_contado)
            transportes.append([transporte_contado, contador, valor])
        
        # Ordeno la lista de mayor a menor
        transportes.sort(reverse = True, key = lambda valor: valor[2])
            
    elif direccion in {"Imports", "Exports"}:
        
        # Obtengo por cada medio de transporte cuantas veces se utilizo y el valor
        # que ha llevado 
        for movimiento in info_movimientos:
            transporte_contado = [direccion, movimiento[7]]
            contador = 0
            valor = 0
            
            # Verifico que no lo haya contado ya
            if transporte_contado in transportes_contados:
                continue
            
            # Cuento las veces que se uso y el valor que movio
            for movimiento_2 in info_movimientos:
                if transporte_contado == [movimiento_2[1], movimiento_2[7]]:
                    contador += 1
                    valor += int(movimiento_2[9])
            
            # Guardo la informacion en listas
            transportes_contados.append(transporte_contado)
            transportes.append([direccion, movimiento[7], contador, valor])
        
        # Ordeno la lista de mayor a menor
        transportes.sort(reverse = True, key = lambda valor: valor[3])
    
    # Regreso la lista que contiene la infromacion de los medios de transporte
    return transportes
     

#################### Opcion 3. Valor total de importaciones y exportaciones ####################

# Funcion que sirve para calcular el valor de los movimientos por pais de origen
def valor_movimientos(direccion = "Imports"):
    """

    Parametros
    ----------
    direccion : TYPE, String
        DESCRIPCION. Por defecto es "Imports", es decir, considera unicamente las
        Importaciones, tambien toma el valor de "Exports" para considerar las exportaciones.


    Returns
    -------
    Lista que contiene los el movimiento, pais, su valor total y el numero de movimientos.

    """
    
    # Inicializo las listas donde se guardara la informacion
    contados = []
    valores_paises = []
    
    # Verifico el valor del argumento recibido
    if direccion == "Exports":
        
        # Cuento el valor de cada pais
        for movimiento in info_movimientos:
            contado = [direccion, movimiento[2]]
            valor = 0
            exportaciones = 0
            
            # Verifico si ya conte el pais
            if contado in contados:
                continue
            
            # Cuento el valor del momiento
            for movimiento_2 in info_movimientos:
                if contado == [movimiento_2[1], movimiento_2[2]]:
                    valor += int(movimiento_2[9])
                    exportaciones += 1
                    
            # Guardo la informacion en las listas
            contados.append(contado)
            if exportaciones == 0:
                continue
            valores_paises.append([direccion, movimiento[2], valor, exportaciones])

        # Ordeno la lista de mayor a menor
        valores_paises.sort(reverse = True, key = lambda valor: valor[2])
    
    elif direccion == "Imports":
        
         # Cuento el valor de cada pais
        for movimiento in info_movimientos:
            contado = [direccion, movimiento[3]]
            valor = 0
            importaciones = 0
            
            # Verifico si ya conte el pais
            if contado in contados:
                continue
            
            # Cuento el valor del momiento
            for movimiento_2 in info_movimientos:
                if contado == [movimiento_2[1], movimiento_2[3]]:
                    valor += int(movimiento_2[9])
                    importaciones += 1
                    
            # Guardo la informacion en las listas
            contados.append(contado)
            if importaciones == 0:
                continue
            valores_paises.append([direccion, movimiento[3], valor, importaciones])

        # Ordeno la lista de mayor a menor
        valores_paises.sort(reverse = True, key = lambda valor: valor[2])
        
    # Regreso la lista que contiene la infromacion
    return valores_paises


# Funcion que me permite calcular un porcentaje del total de la muestra
def paises_generan_porcentaje(lista, porcentaje = .8):
    """

    Parameters
    ----------
    lista : TYPE, list
        DESCRIPCION. Lista a la que se le calcula el porcentaje.
    porcentaje : TYPE, optional
        DESCRIPCION. El valor por defecto es .8, pero puede recibir cualquier
        número en el intervalo cerrado [0, 1]

    Returns
    -------
    Lista que contiene los países que abarcan el porcentaje brindado y porcentaje más próximo al requerido.

    """
    # Inicializo la variable que contendra la suma de los valores
    valor_total = 0
    
    # Obtenemos la suma de total de los movimientos
    for pais in lista:
        valor_total += pais[2]
    
    # Lista que guarda los paises que acumulan dicho porcentaje
    paises = []
    
    # Inicializo una lista que guarda los porcentajes calculados
    porcentajes_calculados = [0]

    #Variable que guarda la suma de los valores
    valor_calculado = 0
    
    # Obtengo los paises que acumulan hasta cierto porcentaje
    for pais in lista:
        valor_calculado += pais[2]
        porcentaje_calculado = round(valor_calculado / valor_total, 5)
        
        # Guardo los datos
        paises.append(pais)
        porcentajes_calculados.append(porcentaje_calculado)
        
        # Verifico si ya se alcanzo el porcentaje deseado
        if porcentaje_calculado <= porcentaje:
            continue
        else:
            
            # Veo cual es el porcentaje mas cercano
            if porcentaje_calculado - porcentaje <= \
                porcentajes_calculados[-2] - porcentaje:
                    break
            else:
                paises.pop(-1)
                porcentajes_calculados.pop(-1)
                break
    
    # Regreeso la lista de los pises
    return paises, porcentajes_calculados[-1]


#################### Menu para el usuario ####################

# Inicializo algunas listas que contendran la informacion
top_10_rutas_imp_anios = []
top_10_rutas_imp = []
top_10_rutas_exp_anios = []
top_10_rutas_exp = []
proporcion_imp = []
proporcion_exp = []
top_transportes = []
top_transportes_imp = []
top_transportes_exp = []

# Muestro la primera interfaz
salir = True
while salir:
    
    # Impimo mensaje de bienvenida
    print('')
    print('|--------------------------------|')
    print('|                                |')
    print('|   Synergy Logistics Opciones   |')
    print('|                                |')
    print('|--------------------------------|')
    print('')
    
    # Opciones del menu
    print("\nSeleccione un numero\n")
    print('1.- Rutas de importacion y exportacion')
    print('2.- Medio de transporte utilizado')
    print('3.- Valor total de importaciones y exportaciones')
    print('0.- Salir')
    opcion = input('Ingrese la opcion seleccionada: ')
    # Dependiendo de la opcion capturada muestro algo diferente
    if opcion == "0":
        print('\n¡Hasta luego!')
        salir = False

    # Opcion 1
    elif opcion == "1":
        salir2 = True
        while salir2:
            print("\nSeleccione un numero\n")
            print('1.- Importaciones')
            print('2.- Exportaciones')
            print('0.- Regresar')
            opcion2 = input('\nIngrese la opcion seleccionada: ')
            # Verifico la opcion seleccionada
            if opcion2 == "0":
                salir2 = False
            # Caso importaciones
            elif opcion2 == "1":
                salir_3 = True
                while salir_3:
                    print("\nSeleccione un numero\n")
                    print('1.- Rutas demandadas')
                    print('2.- Porporcion de demanda')
                    print('0.- Regresar')
                    opcion_3 = input('\nIngrese la opcion seleccionada: ')
                    if opcion_3 == "0":
                        salir_3 = False
                    elif opcion_3 == "1":
                        salir3 = True
                        while salir3:
                            print('\nRegresar "0"')
                            opcion3 = input('¿Desea la temporalidad en anios? [s/n]: ')
                            if opcion3 == "0":
                                salir3 = False
                            elif opcion3 == "s":
                                salir4 = True
                                while salir4:
                                    if top_10_rutas_imp_anios == []:
                                        top_10_rutas_imp_anios = mejores_rutas('Imports', True, True)[0:10]
                                    print('\n-------------------- Top 10 de Rutas mas demandadas de importaciones por anio --------------------\n')
                                    print('Origen | Destino | Anio | Valor | No. Usos')
                                    print('------------------------------------------')
                                    for ruta in top_10_rutas_imp_anios:
                                        print(ruta[1], ' | ', ruta[2], ' | ', ruta[3], ' | ', ruta[4], ' | ', ruta[5])
                                    opcion4 = input('\nRegresar "0": ')
                                    if opcion4 == "0":
                                        salir4 = False
                                    print('\nCaracter INCORRECTO\n')
                            elif opcion3 == "n":
                                salir4 = True
                                while salir4:
                                    if top_10_rutas_imp == []:
                                        top_10_rutas_imp = mejores_rutas('Imports', False, True)[0:10]
                                    print('\n-------------------- Top 10 de Rutas mas demandadas de importaciones --------------------\n')
                                    print('Origen | Destino | Valor | No. Usos')
                                    print('-----------------------------------')
                                    for ruta in top_10_rutas_imp:
                                        print(ruta[1], ' | ', ruta[2], ' | ', ruta[3], ' | ', ruta[4])
                                    opcion4 = input('\nRegresar "0": ')
                                    if opcion4 == "0":
                                        salir4 = False
                                    print('\nCaracter INCORRECTO\n')
                    elif opcion_3 == "2":
                        if proporcion_imp == []:
                            rutas = mejores_rutas("Imports", False)
                            rutas_anios = mejores_rutas("Imports", True)
                            proporcion_imp = proporcion_rutas(rutas, rutas_anios)[0:10]
                        salir4 = True
                        while salir4:
                            print('\n----------- Top 10 proporciones de las rutas de importacion en 2020 -----------\n')
                            print('Origen | Destino | Proporcion del valor | Poporcion de usos')
                            print('-----------------------------')
                            for proporcion in proporcion_imp:
                                print(proporcion[1], ' | ', proporcion[2], ' | ', proporcion[4], ' | ', proporcion[5])
                            opcion4 = input('\nRegresar "0": ')
                            if opcion4 == "0":
                                salir4 = False
                            print('\nCaracter INCORRECTO\n')
                    else: print('\nCaracter INCORRECTO\n')
            # Caso Exportaciones
            elif opcion2 == "2":
                salir_3 = True
                while salir_3:
                    print("\nSeleccione un numero\n")
                    print('1.- Rutas demandadas')
                    print('2.- Proporcion de demanda')
                    print('0.- Regresar')
                    opcion_3 = input('\nIngrese la opcion seleccionada: ')
                    if opcion_3 == "0":
                        salir_3 = False
                    elif opcion_3 == "1":
                        salir3 = True
                        while salir3:
                            print('\nRegresar "0"')
                            opcion3 = input('¿Desea la temporalidad en anios? [s/n]: ')
                            if opcion3 == "0":
                                salir3 = False
                            elif opcion3 == "s":
                                salir4 = True
                                while salir4:
                                    if top_10_rutas_exp_anios == []:
                                        top_10_rutas_exp_anios = mejores_rutas('Exports', True, True)[0:10]
                                    print('\n-------------------- Top 10 de Rutas mas demandadas de exportaciones por anio --------------------\n')
                                    print('Origen | Destino | Anio | Valor | No. Usos')
                                    print('------------------------------------------')
                                    for ruta in top_10_rutas_exp_anios:
                                        print(ruta[1], ' | ', ruta[2], ' | ', ruta[3], ' | ', ruta[4], ' | ', ruta[5])
                                    opcion4 = input('\nRegresar "0": ')
                                    if opcion4 == "0":
                                        salir4 = False
                                    print('\nCaracter INCORRECTO\n')
                            elif opcion3 == "n":
                                salir4 = True
                                while salir4:
                                    if top_10_rutas_exp == []:
                                        top_10_rutas_exp = mejores_rutas('Exports', False, True)[0:10]
                                    print('\n-------------------- Top 10 de Rutas mas demandadas de exportaciones --------------------\n')
                                    print('Origen | Destino | Valor | No. Usos')
                                    print('-----------------------------------')
                                    for ruta in top_10_rutas_exp:
                                        print(ruta[1], ' | ', ruta[2], ' | ', ruta[3], ' | ', ruta[4])
                                    opcion4 = input('\nRegresar "0": ')
                                    if opcion4 == "0":
                                        salir4 = False
                                    print('\nCaracter INCORRECTO\n')
                    elif opcion_3 == "2":
                        if proporcion_exp == []:
                            rutas = mejores_rutas("Exports", False)
                            rutas_anios = mejores_rutas("Exports", True)
                            proporcion_exp = proporcion_rutas(rutas, rutas_anios)[0:10]
                        salir4 = True
                        while salir4:
                            print('\n----------- Top 10 proporciones de las rutas de exportacion en 2020 -----------\n')
                            print('Origen | Destino | Proporcion del valor | Porporcion de usos')
                            print('-----------------------------')
                            for proporcion in proporcion_exp:
                                print(proporcion[1], ' | ', proporcion[2], ' | ', proporcion[4], ' | ', proporcion[5])
                            opcion4 = input('\nRegresar "0": ')
                            if opcion4 == "0":
                                salir4 = False
                            print('\nCaracter INCORRECTO\n')

                    else:
                        print('\nCaracter INCORRECTO\n')

            else:
                print('\nCaracter INCORRECTO\n')

    elif opcion == "2":
        salir2 = True
        while salir2:
            print("\nSeleccione un numero\n")
            print('1.- Importaciones')
            print('2.- Exportaciones')
            print('3.- Total')
            print('0.- Regresar')
            opcion2 = input('\nIngrese la opcion seleccionada: ')
            # Verifico la opcion seleccionada
            if opcion2 == "0":
                salir2 = False
            # Caso importaciones
            elif opcion2 == "1":
                salir3 = True
                while salir3:
                    if top_transportes_imp == []:
                        top_transportes_imp = medio_transporte("Imports")
                    print('\n-------------------- Top medios de transporte de importaciones --------------------\n')
                    print('Medio de transporte | No. usos | Valor importado')
                    print('------------------------------------------------')
                    for transporte in top_transportes_imp:
                        print(transporte[1], ' | ', transporte[2], ' | ', transporte[3])
                    opcion3 = input('\nRegresar "0": ')
                    if opcion3 == "0":
                        salir3 = False
                    print('\nCaracter INCORRECTO\n')
            # Caso exportaciones
            elif opcion2 == "2":
                salir3 = True
                while salir3:
                    if top_transportes_exp == []:
                        top_transportes_exp = medio_transporte("Exports")
                    print('\n-------------------- Top medios de transporte de exportaciones --------------------\n')
                    print('Medio de transporte | No. usos | Valor importado')
                    print('------------------------------------------------')
                    for transporte in top_transportes_exp:
                        print(transporte[1], ' | ', transporte[2], ' | ', transporte[3])
                    opcion3 = input('\nRegresar "0": ')
                    if opcion3 == "0":
                        salir3 = False
                    print('\nCaracter INCORRECTO\n')
            # Caso Total
            elif opcion2 == "3":
                salir3 = True
                while salir3:
                    if top_transportes == []:
                        top_transportes = medio_transporte(False)
                    print('\n-------------------- Top medios de transporte --------------------\n')
                    print('Medio de transporte | No. usos | Valor movido')
                    print('------------------------------------------------')
                    for transporte in top_transportes:
                        print(transporte[0], ' | ', transporte[1], ' | ', transporte[2])
                    opcion3 = input('\nRegresar "0": ')
                    if opcion3 == "0":
                        salir3 = False
                    print('\nCaracter INCORRECTO\n')
                    
    elif opcion == "3":
        salir2 = True
        while salir2:
            print("\nSeleccione un numero\n")
            print('1.- Importaciones')
            print('2.- Exportaciones')
            print('0.- Regresar')
            opcion2 = input('\nIngrese la opcion seleccionada: ')
            # Verifico la opcion seleccionada
            if opcion2 == "0":
                salir2 = False
            # Caso importaciones
            elif opcion2 == "1":
                print('\n¡ADVERTENCIA! Si no ingresa un numero el programa explota.')
                porcentaje = float(input('\nIngrese el porcentaje del valor de importaciones que desea, numero en (0, 1]: '))
                salir3 = True
                while salir3:
                    paises = valor_movimientos('Imports')
                    paises_imp, porcentaje_imp = paises_generan_porcentaje(paises, porcentaje)
                    print(f'\n-------------------- Paises que generan el {round(porcentaje_imp*100,0)}% de las importaciones --------------------\n')
                    print('Pais | No. Importaciones | Valor Importado')
                    print('------------------------------------------')
                    for pais in paises_imp:
                        print(pais[1], ' | ', pais[3], ' | ', pais[2])
                    opcion3 = input('\nRegresar "0": ')
                    if opcion3 == "0":
                        salir3 = False
                    print('\nCaracter INCORRECTO\n')
            # Caso exportaciones
            elif opcion2 == "2":
                print('\n¡ADVERTENCIA! Si no ingresa un numero el programa explota.')
                porcentaje = float(input('\nIngrese el porcentaje del valor de exportaciones que desea, numero en (0, 1]: '))
                salir3 = True
                while salir3:
                    paises = valor_movimientos('Exports')
                    paises_exp, porcentaje_exp = paises_generan_porcentaje(paises, porcentaje)
                    print(f'\n-------------------- Paises que generan el {round(porcentaje_exp*100, 0)}% de las exportaciones --------------------\n')
                    print('Pais | No. Exportaciones | Valor Exportado')
                    print('------------------------------------------')
                    for pais in paises_exp:
                        print(pais[1], ' | ', pais[3], ' | ', pais[2])
                    opcion3 = input('\nRegresar "0": ')
                    if opcion3 == "0":
                        salir3 = False
                    print('\nCaracter INCORRECTO\n')

    else:
        print('\nCaracter INCORRECTO\n')