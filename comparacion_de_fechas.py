def retornar_fecha_mas_antigua(fecha, fecha_a_comparar):

    año_a=int(fecha[6:10])
    año_b=int(fecha_a_comparar[6:10])
    mes_a=int(fecha[3:5])
    mes_b=int(fecha_a_comparar[3:5])
    dia_a=int(fecha[0:2])
    dia_b=int(fecha_a_comparar[0:2])

    if año_b == año_a:
        if mes_b == mes_a:
            if dia_b == dia_a:
                return fecha
            elif dia_b > dia_a:
                return fecha
            else:
                return fecha_a_comparar

    if año_b == año_a:
        if mes_b > mes_a:
            return fecha
        else:
            return fecha_a_comparar
    
    if año_b > año_a:
        return fecha
    else:
        return fecha_a_comparar


def retornar_fecha_mas_reciente(fecha, fecha_a_comparar):

    año_a=int(fecha[6:10])
    año_b=int(fecha_a_comparar[6:10])
    mes_a=int(fecha[3:5])
    mes_b=int(fecha_a_comparar[3:5])
    dia_a=int(fecha[0:2])
    dia_b=int(fecha[0:2])

    if año_b == año_a:
        if mes_b == mes_a:
            if dia_b == dia_a:
                return fecha
            elif dia_b > dia_a:
                return fecha_a_comparar
            else:
                return fecha
            
    if año_b == año_a:
        if mes_b > mes_a:
            return fecha_a_comparar
        else:
            return fecha
            
    if año_b > año_a:
        return fecha_a_comparar
    else:
        return fecha



