from fechas import validar_fecha
from profesiones import listar_profesiones,validar_eleccion
from tipos_origen_de_fondos import listar_origen_fondos,validar_lista_origen

def ingresar_datos():

    contribuyentes=[]

    continuar = 'siguiente'

    while(continuar == 'siguiente'):
        nombre=input("Ingrese su nombre: ")

        apellido=input("Ingrese su apellido: ")

        dni=int(input("Ingrese su D.N.I.: "))

        fecha_naci=input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        validar_fecha(fecha_naci)

        edad=int(input("Ingrese su edad: "))
        while 1<edad>180:
            edad=int(input("Ingrese su edad: "))

        listar_profesiones()
        eleccion = int(input("Ingrese el número de la profesión que desea elegir: "))
        validar_eleccion(eleccion)
        if eleccion==37 :
            prof_otro=input("Ingrese su profesión:")
        #print("Su profesión es:",listar_profesiones[eleccion-1])
       
        fecha_decla=input("Ingrese la fecha de declaración (DD/MM/AAAA): ")
        validar_fecha(fecha_decla)

        monto_decla=float(input("Ingrese el monto a declarar: "))

        listar_origen_fondos()
        fondo = int(input("Ingrese el número del tipo de origen de fondo que va a declarar: "))
        validar_lista_origen(fondo)
        #print("El tipo de origen de fondo es:",listar_origen_fondos[fondo-1])

        continuar=input("Pasa ingresar otro contribuyente ingrese siguiente o ingrese finalizar para terminar: ")
                


        