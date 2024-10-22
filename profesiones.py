def prof_eleccion():

    profesiones=[
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

    print("Selecciones una profesión")
    for profesion in profesiones:
        print(profesion)
    eleccion = int(input("Ingrese el número de la profesión que desea elegir: "))
    if eleccion==37 :
        prof_otro=input("Ingrese su profesión:")
    while 1<eleccion>37:
        eleccion = int(input("Opción inválida. Ingrese un número entre 1 y 37: "))

