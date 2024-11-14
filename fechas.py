def validar_fecha(fecha):
    fecha_a_validar = fecha

    dia=int(fecha_a_validar[0:2])
    mes=int(fecha_a_validar[3:5])
    año=int(fecha_a_validar[6:10])

    while (dia<1 or dia>31) or (mes<1 or mes>12) or (año<1900 or año>2025):
        if dia<1 or dia>31:
            print("El día ingresado es invalido")

        if mes<1 or mes>12:
            print("El mes ingresado es invalido")

        if año<1900 or año>2025:
            print("El año ingresado es invalido")
        
        fecha_a_validar = input("Ingrese la fecha nuevamente (DD/MM/AAAA): ")   
        dia=int(fecha_a_validar[0:2])
        mes=int(fecha_a_validar[3:5])
        año=int(fecha_a_validar[6:10])
    return fecha_a_validar
