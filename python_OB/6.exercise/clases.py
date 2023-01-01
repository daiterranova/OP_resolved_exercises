""" En este ejercicio vais a crear la clase Vehículo la cual tendrá
los siguientes atributos:
Color
Ruedas
Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y
tendrá los siguientes atributos:
Velocidad
Cilindrada
Por último, tendrás que crear un objeto de la clase Coche
y mostrarlo por consola. """


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, {} ruedas, {} puertas, velocidad {} y {} cilindradas".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


car = Coche("blue", 4, 5, 110, 200)
car.__str__()
print(car)
