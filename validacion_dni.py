def validar_dni(dni):
    while dni < 10000000 or dni > 99999999:
        print(f"El numero de dni {dni} es invalido")
        dni = int(input("Ingrese su numero de dni, debe contener 8 digitos: "))
    return dni 