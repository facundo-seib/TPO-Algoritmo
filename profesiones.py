
PROFESIONES=[
        "Médico",
        "Enfermero/a",
        "Dentista",
        "Psicólogo/a",
        "Ingeniero/a civil",
        "Ingeniero/a de software",
        "Ingeniero/a mecánico",
        "Arquitecto/a",
        "Técnico/a en electrónica",
        "Trabajador/a social",
        "Maestro/a",
        "Profesor/a",
        "Artista plástico",
        "Diseñador/a gráfico",
        "Fotógrafo/a",
        "Músico/a",
        "Actor/actriz",
        "Contador/a",
        "Administrador/a de empresas",
        "Analista financiero",
        "Marketing manager",
        "Químico/a",
        "Biólogo/a",
        "Físico/a",
        "Matemático/a",
        "Desarrollador/a web",
        "Especialista en ciberseguridad",
        "Analista de sistemas",
        "Administrador/a de bases de datos",
        "Abogado/a",
        "Notario/a",
        "Juez/a",
        "Fiscal",
        "Chef",
        "Estilista",
        "Agente de ventas",
        "Otro"
    ]

def listar_profesiones():

    print("Seleccione una profesión")
    i = 1
    for profesion in PROFESIONES:
        print(f'{i}. {profesion}')
        i = i+1

#nuevo
def validar_eleccion(eleccion):
    
    while (eleccion=='') or (not eleccion.isnumeric()) or (int(eleccion)<1 or int(eleccion)>37):
        eleccion = input("Opción inválida. Ingrese un número entre 1 y 37: ")
    return int(eleccion)
        

def rankear_profesiones(ranking):
    copia_profesiones = PROFESIONES
    n = len(ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ranking[j] < ranking[j + 1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
                copia_profesiones[j], copia_profesiones[j + 1] = copia_profesiones[j + 1], copia_profesiones[j]

    for i in range(n):
        print(f"{i + 1}. {copia_profesiones[i]} - Veces ingresada: {ranking[i]}")
