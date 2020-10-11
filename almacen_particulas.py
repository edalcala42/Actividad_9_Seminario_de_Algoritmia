from particula import Particula

class Almacen_Particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(123, 10, 25, 45, 36, 90, 15, 20, 36, 8.6)
p02 = Particula(456, 6, 2, 30, 10, 80, 55, 90, 76, 1.6)

conjunto_de_particulas = Almacen_Particulas()

conjunto_de_particulas.agregar_final(p01)
conjunto_de_particulas.agregar_inicio(p02)
conjunto_de_particulas.agregar_inicio(p01)

conjunto_de_particulas.mostrar()