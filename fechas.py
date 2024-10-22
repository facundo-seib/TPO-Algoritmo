def validar_fecha(fecha):

    dia=int(fecha[0:2])
    while dia<1 and dia>31:
        fecha=input("El día ingresado es invalido, ingrese la fecha nuevamente (DD/MM/AAAA): ")
        dia=int(fecha[0:2])

    mes=int(fecha[3:5])
    while mes<1 and mes>12:
        fecha=input("El mes ingresado es invalido, ingrese la fecha nuevamente (DD/MM/AAAA): ")
        mes=int(fecha[3:5])

    año=int(fecha[6:8])
    while año<1900 and año>2025:
        fecha=input("El año ingresado es invalido, ingrese la fecha nuevamente (DD/MM/AAAA):")
        año=int(fecha[6:8])


