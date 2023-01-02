""" Crea un script que 
le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
 """

countries = input("Give a list of countries separate each by commas")
list = countries.split(",")
filtered_list = set(list)
sorted_list = sorted(filtered_list)
print(sorted_list)
