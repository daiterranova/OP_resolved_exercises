""" Escribe una función que pueda decirte si un año (número entero) es bisiesto o no. """


def leap_year(year):
    # si  condicion da True => (True) and (True or True)
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        # str convierte a string el año para poder concatenarlo
        return str(year) + " es bisiesto"
    else:
        return str(year) + " no es bisiesto"


print(leap_year(1900))
print(leap_year(2400))
print(leap_year(1600))
