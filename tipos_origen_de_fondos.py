TIPOS_ORIGEN_FONDOS=[
        "1. Bienes inmuebles",
        "2. Bienes muebles",
        "3. Depósitos y cuentas bancarias",
        "4. Inversiones financieras",
        "5. Activos empresariales",
        "6. Pesos en efectivo",
        "7. Moneda extranjera en efectivo",
        "8. Objetos de valor",
    ]
        
def listar_origen_fondos():

    print("Selecciona cuál es tu origen de fondo a declarar")
    for origen_de_fondo in TIPOS_ORIGEN_FONDOS:
        print(origen_de_fondo)

def validar_lista_origen(fondo):
    
    while fondo<1 and fondo>7:
        fondo = int(input("Opción inválida. Ingrese un número entre 1 y 7: "))

