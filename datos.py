from fechas import validar_fecha
from profesiones import listar_profesiones,validar_eleccion,PROFESIONES, rankear_profesiones
from tipos_de_fondos import listar_tipos_fondos,validar_lista_tipos, TIPOS_FONDOS, listar_mayor_y_menor_cantidad_de_fondos
from origen_de_fondos import listar_origen_fondos,validar_lista_origen, ORIGEN_FONDOS, rankear_origenes
from comparacion_de_fechas import retornar_fecha_mas_antigua, retornar_fecha_mas_reciente
from otras_validaciones import validar_dni, validar_monto
def ingresar_datos():
    contribuyentes = []
    contribuyentes_dni = []

    fecha_mas_antigua = None
    fecha_mas_reciente = None

    rankingProfesiones = [0]*len(PROFESIONES)
    rankingOrigen = [0]*len(ORIGEN_FONDOS)
    rankingTipos = [0]*len(TIPOS_FONDOS)

    contadorDeContribuyentes = 0

    acumuladorDeEdad = 0
    menorEdad = 0
    mayorEdad = 0

    acumuladorDeMonto = 0
    menorMonto = 0
    mayorMonto = 0

    # Parte de los porcentajes declarados en argentian y en el exterior
#nuevo
    ContadorDeDeclaracionesArg = 0
    ContadorDeDeclaracionesExt = 0

    total_bienes_decla_argentina = 0
    total_bienes_decla_exterior = 0 

    total_bienes_argentina = 0
    total_bienes_exterior = 0 

    declarado_en_arg = 'Argentina'
    declarado_en_exterior = 'exterior'
    # Aca termina la parte de los porcentajes declarados en argentina y en el exterior

    continuar = 'y'

    while(continuar == 'y'):
        contadorDeContribuyentes = contadorDeContribuyentes + 1
        contribuyente_actual = '\n'
        

# NOMBRE Y APELLIDO
        nombre=input("Ingrese su nombre: ")
        while nombre=='':
            nombre=input("Por favor, ingrese su nombre para continuar: ")
        contribuyente_actual = contribuyente_actual + 'Nombre: ' +  nombre + '\n'

        apellido=input("Ingrese su apellido: ")
        while apellido=='':
            apellido=input("Por favor, ingrese su apellido para continuar: ")
        contribuyente_actual = contribuyente_actual + 'Apellido: ' +  apellido + '\n'

# DNI
        dni=input("Ingrese su D.N.I.: ")
        dni = validar_dni(dni)
        contribuyentes_dni.append(dni)
        contribuyente_actual = contribuyente_actual + 'DNI: ' +  dni + '\n'


#FECHA DE NACIMIENTO
        fecha_naci=input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        while fecha_naci=='':
            fecha_naci=input("Por favor, ingrese su fecha de nacimiento para continuar (DD/MM/AAAA): ")
        validar_fecha(fecha_naci)
        contribuyente_actual = contribuyente_actual + 'Fecha de nacimiento: ' +  fecha_naci + '\n'

#EDAD
        edad=input("Ingrese su edad: ")
        while edad== '':
            edad=input("Por favor, ingrese su edad para continuar: ")
        while not edad.isnumeric():
            edad=input("Por favor, ingrese su edad en numeros para continuar: ")
        contribuyente_actual = contribuyente_actual + 'Edad: ' +  edad + '\n'
        edad = int(edad)
        if edad<17:
            edad=int(input("No puede declarar siendo menor de edad. Intentelo de nuevo: "))
        if menorEdad == 0 or menorEdad > edad:
            menorEdad = edad
        if mayorEdad < edad:
            mayorEdad = edad
        acumuladorDeEdad = acumuladorDeEdad + edad

#PROFESIONES
        listar_profesiones()
        eleccion = input("Ingrese el número de la profesión que desea elegir: ")
        eleccion = validar_eleccion(eleccion)
        if eleccion == 37:
            prof_otro=input("Ingrese su profesión:")
            print("Su profesión es: ", prof_otro)
            contribuyente_actual = contribuyente_actual + 'Profesión: ' +  prof_otro + '\n'
        else:
            print("Su profesión es: ", PROFESIONES[eleccion - 1])
            contribuyente_actual = contribuyente_actual + 'Profesión: ' +  PROFESIONES[eleccion - 1] + '\n'

        rankingProfesiones[eleccion-1] = rankingProfesiones[eleccion-1] + 1
        
#FECHA DECLARACION
        fecha_decla=input("Ingrese la fecha de declaración (DD/MM/AAAA): ")
        while(fecha_decla == ''):
            fecha_decla=input("La fecha de declaracion no puede estar vacia. Vuelva a intentarlo (DD/MM/AAAA): ")

        validar_fecha(fecha_decla)
        contribuyente_actual = contribuyente_actual + 'Fecha de declaracion: ' +  fecha_decla + '\n'

        if fecha_mas_antigua == None:
            fecha_mas_antigua = fecha_decla
        else:
            fecha_mas_antigua = retornar_fecha_mas_antigua(fecha_mas_antigua, fecha_decla)

        if fecha_mas_reciente == None:
            fecha_mas_reciente = fecha_decla
        else:
            fecha_mas_reciente = retornar_fecha_mas_reciente(fecha_mas_reciente, fecha_decla)

#MONTO
        monto_decla=input("Ingrese el monto a declarar: ")
        monto_decla = validar_monto(monto_decla)
        contribuyente_actual = contribuyente_actual + 'Monto: $' +  monto_decla + '\n'

        monto_decla = float(monto_decla)
        if menorMonto == 0 or menorMonto > monto_decla:
            menorMonto = monto_decla
        if mayorMonto < monto_decla:
            mayorMonto = monto_decla
        acumuladorDeMonto = acumuladorDeMonto + monto_decla

        # Parte donde se hacen los porcentajes de los bienes declarados en argentina o en el exterior

#nuevo
        lugar_declaracion = input("Ingrese el lugar donde va a declarar los bienes, Si es Argentina debe escribir 'Argentina', sino debe ingresar 'exterior': ")
        while lugar_declaracion != declarado_en_arg and lugar_declaracion != declarado_en_exterior:
            lugar_declaracion = input(f"El lugar de declaracion es incorrecto, para poder continuar debe ingresar {declarado_en_arg} o {declarado_en_exterior}: ")
        contribuyente_actual = contribuyente_actual + 'Lugar de declaracion: ' +  lugar_declaracion + '\n'

        if lugar_declaracion == declarado_en_arg:
            ContadorDeDeclaracionesArg += 1
            total_bienes_decla_argentina = monto_decla
            total_bienes_argentina += total_bienes_decla_argentina
        else:
            ContadorDeDeclaracionesExt += 1 
            total_bienes_decla_exterior = monto_decla
            total_bienes_exterior += total_bienes_decla_exterior

        bienes_totales = total_bienes_exterior + total_bienes_argentina

        porcentaje_argentina = (total_bienes_argentina / bienes_totales) * 100
        procentaje_exterior = (total_bienes_exterior / bienes_totales) * 100


        listar_tipos_fondos()
        fondo = input("Ingrese el número del tipo de fondo que va a declarar: ")
        fondo = validar_lista_tipos(fondo)
        print("El tipo de fondo es:", TIPOS_FONDOS[fondo-1])
        contribuyente_actual = contribuyente_actual + 'Tipo de fondo: ' +  TIPOS_FONDOS[fondo-1] + '\n'
        rankingTipos[fondo-1] = rankingTipos[fondo-1] + 1

        listar_origen_fondos()
        origen = input("Ingrese el número del tipo de origen de fondo que va a declarar: ")
        origen = validar_lista_origen(origen)
        print("El tipo de origen de fondo es:", ORIGEN_FONDOS[origen-1])
        contribuyente_actual = contribuyente_actual + 'Origen de fondos: ' +  ORIGEN_FONDOS[origen-1] + '\n'

        rankingOrigen[origen-1] = rankingOrigen[origen-1] + 1
        contribuyentes.append(contribuyente_actual)
        continuar=input("Desea ingresar otro contribuyente? (y/n): ")
        print('\n\n')

    busqueda=input("Desea buscar un contribuyente por DNI? (y/n): ")

    if busqueda == 'y':
        while busqueda == 'y':
            dni_a_buscar = input("Ingrese el DNI del contribuyente a buscar: ")
            array_search_done = False
            contribuyente_encontrado = False
            i = len(contribuyentes_dni)-1
            while not array_search_done: 
                if contribuyentes_dni[i] == dni_a_buscar:
                    array_search_done = True
                    contribuyente_encontrado = contribuyentes[i]
                else:
                    i = i-1
                
                if i == -1:
                    contribuyente_encontrado = "No se encontro el contribuyente solicitado"
                    array_search_done = True
            print(contribuyente_encontrado)
            busqueda=input("Desea buscar otro contribuyente por DNI? (y/n): ")

                

#PRINTS
    print(f"La cantidad de personas registradas en el proceso fueron: {contadorDeContribuyentes}") 
    print(f"La menor edad registrada en el ingreso de datos es de: {menorEdad} años.")
    print(f"La mayor edad registrada en el ingreso de datos es de: {mayorEdad} años.")
    print(f"La edad promedio en el ingreso de datos es de: {acumuladorDeEdad / contadorDeContribuyentes} años.")
    print(f"La fecha de declaración más lejana en el ingreso de datos es: {fecha_mas_antigua}")
    print(f"La fecha de declaración más cercana en el ingreso de datos es: {fecha_mas_reciente}")
    print(f"El menor monto declarado es de: ${menorMonto}, el mayor es de ${mayorMonto} y el promedio es de ${acumuladorDeMonto / contadorDeContribuyentes}")
    print(f"Total bienes en Argentina: {ContadorDeDeclaracionesArg}")
    print(f"Total bienes en el exterior: {ContadorDeDeclaracionesExt}")
    print(f"El porcentaje de bienes declarados en argentina es de: {porcentaje_argentina:.2f}%")
    print(f"El porcentaje de bienes declarados en el exterior es de: {procentaje_exterior:.2f}%")
    listar_mayor_y_menor_cantidad_de_fondos(rankingTipos)
    print('')
    print("\033[1mRANKING DE PROFESIONES\033[0m")

    rankear_profesiones(rankingProfesiones)
    print('')
    print("\033[1mRANKING DE FONDOS\033[0m")
    rankear_origenes(rankingOrigen)
    



        