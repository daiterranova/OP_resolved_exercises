""" En este segundo ejercicios tendréis que 
crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. 
Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7,
     se mostrará un mensaje y 
en caso contrario, 
    haréis una operación para calcular el tiempo que queda de trabajo. """

# paso 1 => importar modulo time
# paso 2 => necesito acceder la fecha del sistema
# paso 3 => necesito poder comprobar la hora
# paso 4 => si son mas de las 7
# paso 5 => muestra algo
# paso 6 => sino
import time
# calcular cuanto falta para las 7
# diferencia entre el tiempo actual y las 7

# paso 1
""" from time import time, ctime """
# paso 2

sec = time.time()  # me traigo el tiempo en segundos
print(sec)
# convierte los segundos a la fecha y hora local
local_time = time.localtime(sec)
print(local_time)
# me quedo solo con el valor que corresponde a la hora
local_hour = local_time.tm_hour
local_minutes = local_time.tm_min
time_home = 19


def what_time():
    if local_hour > time_home:
        return ("time to go home")
    else:
        rest_time_hour = 18 - local_hour
        rest_time_min = 59 - local_minutes
        print("Faltan " + str(rest_time_hour) + " horas y " +
              str(rest_time_min) + " minutos para ir a casa")


what_time()
