from fechas import validar_fecha

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

        #Hice una lista aparte pero nose ejecuta la funcion
        from profesiones import prof_eleccion
        prof_eleccion()

        fecha_decla=input("Ingrese la fecha de declaración (DD/MM/AAAA): ")
        validar_fecha(fecha_decla)

        monto_decla=float(input("Ingrese el monto a declarar: "))

        ori_fondo=input("Ingrese el orígen de los fondos: ")
        # es necesario hacer una lista de los origenes que se puedan declarar?

        continuar=input("Pasa ingresar otro contribuyente ingrese siguiente o ingrese finalizar para terminar: ")
                


                
    contribuyentes.append(nombre)
    contribuyentes.append(apellido)
    contribuyentes.append(dni)
    contribuyentes.append(fecha_naci)
    contribuyentes.append(edad)
    contribuyentes.append(prof)
    contribuyentes.append(fecha_decla)
    contribuyentes.append(monto_decla)
    contribuyentes.append(ori_fondo)    


    print(contribuyentes)
        