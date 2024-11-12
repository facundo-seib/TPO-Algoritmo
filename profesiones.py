
PROFESIONES=[
        "1. Médico",
        "2. Enfermero/a",
        "3. Dentista",
        "4. Psicólogo/a",
        "5. Ingeniero/a civil",
        "6. Ingeniero/a de software",
        "7. Ingeniero/a mecánico",
        "8. Arquitecto/a",
        "9. Técnico/a en electrónica",
        "10. Trabajador/a social",
        "11. Maestro/a",
        "12. Profesor/a",
        "13. Artista plástico",
        "14. Diseñador/a gráfico",
        "15. Fotógrafo/a",
        "16. Músico/a",
        "17. Actor/actriz",
        "18. Contador/a",
        "19. Administrador/a de empresas",
        "20. Analista financiero",
        "21. Marketing manager",
        "22. Químico/a",
        "23. Biólogo/a",
        "24. Físico/a",
        "25. Matemático/a",
        "26. Desarrollador/a web",
        "27. Especialista en ciberseguridad",
        "28. Analista de sistemas",
        "29. Administrador/a de bases de datos",
        "30. Abogado/a",
        "31. Notario/a",
        "32. Juez/a",
        "33. Fiscal",
        "34. Chef",
        "35. Estilista",
        "36. Agente de ventas",
        "37. Otro"
    ]

def listar_profesiones():

    print("Seleccione una profesión")
    for profesion in PROFESIONES:
        print(profesion)

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
