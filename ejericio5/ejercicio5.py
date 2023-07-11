def es_bisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2020
resultado = es_bisiesto(year)
print('El año', year, 'es bisiesto', resultado)
