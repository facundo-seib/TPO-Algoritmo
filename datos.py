from fechas import validar_fecha
from profesiones import listar_profesiones,validar_eleccion,PROFESIONES
from tipos_origen_de_fondos import listar_origen_fondos,validar_lista_origen, TIPOS_ORIGEN_FONDOS
from comparacion_de_fechas import retornar_fecha_mas_antigua, retornar_fecha_mas_reciente

def ingresar_datos():

    fecha_mas_antigua = None
    fecha_mas_reciente = None

    contadorDeContribuyentes = 0

    acumuladorDeEdad = 0
    menorEdad = 0
    mayorEdad = 0

    acumuladorDeMonto = 0
    menorMonto = 0
    mayorMonto = 0

    continuar = 'siguiente'

    while(continuar == 'siguiente'):
        contadorDeContribuyentes = contadorDeContribuyentes + 1

        nombre=input("Ingrese su nombre: ")
        while nombre=='':
            nombre=input("Por favor, escriba su nombre para continuar: ")

        apellido=input("Ingrese su apellido: ")
        while apellido=='':
            apellido=input("Por favor, escriba su apellido para continuar: ")

        dni=(input("Ingrese su D.N.I.: "))
        while dni=='':
            dni=input("Por favor, escriba su D.N.I. para continuar: ")

        fecha_naci=input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        validar_fecha(fecha_naci)

        edad=int(input("Ingrese su edad: "))
        while edad<17:
            edad=int(input("No puede declarar siendo menor de edad. Intentelo de nuevo: "))
        if menorEdad == 0 or menorEdad > edad:
            menorEdad = edad
        if mayorEdad < edad:
            mayorEdad = edad
        acumuladorDeEdad = acumuladorDeEdad + edad

        listar_profesiones()
        eleccion = int(input("Ingrese el número de la profesión que desea elegir: "))
        validar_eleccion(eleccion)
        if eleccion==37 :
            prof_otro=input("Ingrese su profesión:")
        print("Su profesión es:",PROFESIONES[eleccion-1])

        fecha_decla=input("Ingrese la fecha de declaración (DD/MM/AAAA): ")
        validar_fecha(fecha_decla)
        if fecha_mas_antigua == None:
            fecha_mas_antigua = fecha_decla
        else:
            fecha_mas_antigua = retornar_fecha_mas_antigua(fecha_mas_antigua, fecha_decla)

        if fecha_mas_reciente == None:
            fecha_mas_reciente = fecha_decla
        else:
            fecha_mas_reciente = retornar_fecha_mas_reciente(fecha_mas_reciente, fecha_decla)

        monto_decla=float(input("Ingrese el monto a declarar: "))
        while monto_decla < 0 :
            monto_decla=float(input("Monto invalido, Ingrese un monto valido: "))            
        if menorMonto == 0 or menorMonto > monto_decla:
            menorMonto = monto_decla
        if mayorMonto < monto_decla:
            mayorMonto = monto_decla
        acumuladorDeMonto = acumuladorDeMonto + monto_decla

        listar_origen_fondos()
        fondo = int(input("Ingrese el número del tipo de origen de fondo que va a declarar: "))
        validar_lista_origen(fondo)
        print("El tipo de origen de fondo es:", TIPOS_ORIGEN_FONDOS[fondo-1])

        continuar=input("Pasa ingresar otro contribuyente ingrese siguiente o ingrese finalizar para terminar: ")

    print(f"La cantidad de personas registradas en el proceso fueron: {contadorDeContribuyentes}") 
    print(f"La menor edad registrada en el ingreso de datos es de: {menorEdad} años.")
    print(f"La mayor edad registrada en el ingreso de datos es de: {mayorEdad} años.")
    print(f"La edad promedio en el ingreso de datos es de: {acumuladorDeEdad / contadorDeContribuyentes} años.")
    print(f"La fecha de declaración más lejana en el ingreso de datos es: {fecha_mas_antigua}")
    print(f"La fecha de declaración más cercana en el ingreso de datos es: {fecha_mas_reciente}")
    print(f"El menor monto declarado es de: ${menorMonto}, el mayor es de ${mayorMonto} y el promedio es de ${acumuladorDeMonto / contadorDeContribuyentes}")
    



        