ORIGEN_FONDOS=[
        "1. Ingresos de actividades lícitas (salarios, rentas, ganancias de inversiones)",
        "2. Herencias o donaciones",
        "3. Venta de activos (propiedades, bienes muebles, acciones)",
        "4. Ahorros o fondos personales",
        "5. Inversiones extranjeras o bienes fuera del país",
        "6. Operaciones financieras informales o no registradas",
        "7. Fondeo o reestructuración de deuda (préstamos, refinanciación de deudas)",
        "8. Fondos provenientes de actividades no declaradas",
    ]
        
def listar_origen_fondos():

    print("Selecciona cuál es el origen del fondo a declarar")
    for origen in ORIGEN_FONDOS:
        print(origen)

    

def validar_lista_origen(origen):
    
    while origen == '' or not origen.isnumeric() or (int(origen)<1 and int(origen)>7):
        origen = input("Opción inválida. Ingrese un número entre 1 y 7: ")
    return int(origen)

def rankear_origenes(ranking):
    copia_fondos = ORIGEN_FONDOS
    n = len(ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ranking[j] < ranking[j + 1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
                copia_fondos[j], copia_fondos[j + 1] = copia_fondos[j + 1], copia_fondos[j]

    for i in range(n):
        print(f"{i + 1}. {copia_fondos[i]} - Veces ingresado: {ranking[i]}")

