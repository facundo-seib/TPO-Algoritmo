TIPOS_FONDOS=[
        "Bienes inmuebles",
        "Bienes muebles",
        "Depósitos y cuentas bancarias",
        "Inversiones financieras",
        "Activos empresariales",
        "Pesos en efectivo",
        "Moneda extranjera en efectivo",
        "Objetos de valor",
    ]
        
def listar_tipos_fondos():

    print("Selecciona cuál es tu tipo de fondo a declarar")
    i = 1
    for tipo_de_fondo in TIPOS_FONDOS:
        print(f'{i}. {tipo_de_fondo}')
        i = i+1

def validar_lista_tipos(fondo):
    
    while fondo == '' or not fondo.isnumeric() or (int(fondo)<1 and int(fondo)>7):
        fondo = input("Opción inválida. Ingrese un número entre 1 y 7: ")
    return int(fondo)

def listar_mayor_y_menor_cantidad_de_fondos(ranking):
    copia_fondos = TIPOS_FONDOS
    n = len(ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ranking[j] < ranking[j + 1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
                copia_fondos[j], copia_fondos[j + 1] = copia_fondos[j + 1], copia_fondos[j]

    print(f"El activo que se ingreso mas veces es: {copia_fondos[0]} - Veces ingresada: {ranking[0]}")
    print(f"El activo que se ingreso menos veces es: {copia_fondos[n-1]} - Veces ingresada: {ranking[n-1]}")


