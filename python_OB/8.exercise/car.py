""" En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos. """

import pickle


class Car():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def getData(self):
        return f"{self.brand} year {self.year}"


car = Car("Chevrolet", 1990)
car.getData()

# serializar la clase en data.bin
""" file = open("data.bin", "wb")
pickle.dump(car, file)
file.close() """

# recuperar la data
file = open("data.bin", "rb")
car = pickle.load(file)
file.close()
