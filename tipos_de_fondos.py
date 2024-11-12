TIPOS_FONDOS=[
        "1. Bienes inmuebles",
        "2. Bienes muebles",
        "3. Depósitos y cuentas bancarias",
        "4. Inversiones financieras",
        "5. Activos empresariales",
        "6. Pesos en efectivo",
        "7. Moneda extranjera en efectivo",
        "8. Objetos de valor",
    ]
        
def listar_tipos_fondos():

    print("Selecciona cuál es tu tipo de fondo a declarar")
    for tipo_de_fondo in TIPOS_FONDOS:
        print(tipo_de_fondo)

def validar_lista_tipos(fondo):
    
    while fondo<1 and fondo>7:
        fondo = int(input("Opción inválida. Ingrese un número entre 1 y 7: "))

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


