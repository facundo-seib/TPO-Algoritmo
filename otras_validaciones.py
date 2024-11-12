def validar_dni(dni):
    while dni == '' or not dni.isnumeric() or (int(dni) < 1000000 or int(dni) > 99999999):
        print(f"El numero de dni: '{dni}' es invalido")
        dni = input("Ingrese su numero de dni, debe contener 7 u 8 digitos: ")
    return int(dni) 

def validar_monto(monto):
    while monto == '' or (not monto.isnumeric()) or (float(monto) < 0) :
        monto=input("Monto invalido, Ingrese un monto valido: ")  
    return float(monto)    