from fechas import validar_fecha
from profesiones import listar_profesiones,validar_eleccion,PROFESIONES
from tipos_origen_de_fondos import listar_origen_fondos,validar_lista_origen, TIPOS_ORIGEN_FONDOS
from comparacion_de_fechas import retornar_fecha_mas_antigua, retornar_fecha_mas_reciente
from validacion_dni import validar_dni
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

    # Parte de los porcentajes declarados en argentian y en el exterior
#nuevo
    ContadorDeDeclaracionesArg = 0
    ContadorDeDeclaracionesExt = 0

    total_bienes_decla_argentina = 0
    total_bienes_decla_exterior = 0 

    total_bienes_argentina = 0
    total_bienes_exterior = 0 

    declarado_en_arg = 'argentina'
    declarado_en_exterior = 'exterior'
    # Aca termina la parte de los porcentajes declarados en argentina y en el exterior


    continuar = 'siguiente'

    while(continuar == 'siguiente'):
        contadorDeContribuyentes = contadorDeContribuyentes + 1

        nombre=input("Ingrese su nombre: ")
        while nombre=='':
            nombre=input("Por favor, ingrese su nombre para continuar: ")

        apellido=input("Ingrese su apellido: ")
        while apellido=='':
            apellido=input("Por favor, ingrese su apellido para continuar: ")

# nuevo
        dni=int(input("Ingrese su D.N.I.: "))
        dni = validar_dni(dni)
        while dni=='':
            dni=int(input("Por favor, ingrese su D.N.I. para continuar: "))
            dni = validar_dni(dni)
        fecha_naci=input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        while fecha_naci=='':
            fecha_naci=input("Por favor, ingrese su fecha de nacimiento para continuar (DD/MM/AAAA): ")
        validar_fecha(fecha_naci)

#nuevo
        edad=input("Ingrese su edad: ")
        while edad== '':
            edad=input("Por favor, ingrese su edad para continuar: ")
        edad=int(edad)
            
        if edad<17:
            edad=int(input("No puede declarar siendo menor de edad. Intentelo de nuevo: "))
        if menorEdad == 0 or menorEdad > edad:
            menorEdad = edad
        if mayorEdad < edad:
            mayorEdad = edad
        acumuladorDeEdad = acumuladorDeEdad + edad

#nuevo
        listar_profesiones()
        eleccion = int(input("Ingrese el número de la profesión que desea elegir: "))
        eleccion = validar_eleccion(eleccion)
        if eleccion == 37:
            prof_otro=input("Ingrese su profesión:")
            print("Su profesión es: ", prof_otro)
        else:
            print("Su profesión es: ", PROFESIONES[eleccion - 1])
        

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

        # Parte donde se hacen los porcentajes de los bienes declarados en argentina o en el exterior

#nuevo
        lugar_declaracion = input("Ingrese el lugar donde va a declarar los bienes, Si es Argentina debe escribir 'argentina', sino debe ingresar 'exterior': ")
        while lugar_declaracion != declarado_en_arg and lugar_declaracion != declarado_en_exterior:
            lugar_declaracion = input(f"El lugar de declaracion es incorrecto, para poder continuar debe ingresar {declarado_en_arg} o {declarado_en_exterior}: ")
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
#nuevo    
    print(f"Total bienes en Argentina: ${total_bienes_argentina:.0f}")
    print(f"Total bienes en el exterior: ${total_bienes_exterior:.0f}")
    print(f"El porcentaje de bienes declarados en argentina es de: {porcentaje_argentina:.2f}%")
    print(f"El porcentaje de bienes declarados en el exterior es de: {procentaje_exterior:.2f}%") 
    # el activo regularizado que mas se repite es..
    # el activo regularizado que menos se repite es..
    



        