__author__ = 'Julián'

class Prestamo():
    def __init__(self, cuotas, importe, interes):
        self.__cuotas = cuotas
        self.__importeTotal = importe + (importe * interes)
        self.__cuota = self.__importeTotal / cuotas
        self.__interes = interes

    @property
    def cuota(self):
        return self.__cuota

    def get_num_cuotas(self):
        return self.__cuotas

    def paga_cuota(self):
        self.__importeTotal -= self.cuota
        self.__cuotas -= 1

    def amortiza(self, x):
        self.__importeTotal -= x
        self.__cuota = self.__importeTotal / self.__cuotas

    def __str__(self):
        return ("Importe Total = {0}\n"
                "Cuotas Restantes = {1}\n"
                "Valor cuota = {2}\n"
                "Intereses = {3}"
                .format(self.__importeTotal,self.__cuotas,
                        self.__cuota, self.__interes))
"""
prest = Prestamo(5,200,0.05)
print(prest)
prest.amortiza(100)
print("Prestamo despues de amortizar 100")
print (prest)

prest.paga_cuota()
print("Cuota pagada")
print (prest)
"""

class Pieza():
    def __init__(self, id):
        self.__id = id

    def __str__(self):
        return "Pieza: {0}".format(id)

class Tuerca(Pieza):
    def __init__(self, id, diametro):
        super().__init__(id)
        self.__dia = diametro

    def __str__(self):
        return super().__str__() + " | Tuerca diametro: {0}"\
            .format(self.__dia)

class Tuberia(Pieza):
    def __init__(self, id, longitud):
        super().__init__(id)
        self.__long = longitud

    def __str__(self):
        return super().__str__() + " | Tuberia longitud: {0}"\
            .format(self.__long)

class Codo(Pieza):
    def __init__(self, id, angulo):
        super().__init__(id)
        self.__ang = angulo

    def __str__(self):
        return super().__str__() + " | Codo angulo: {0}"\
            .format(self.__ang)

class Inventario():
    def __init__(self):
        self.__inventario = []

    def __add__(self, other):
        self.__inventario.append(other)

    def __sub__(self, other):
        self.__inventario.__delitem__(other)

    def __mod__(self, other, pos):
        self.__inventario[pos] = other

    def __str__(self):
        return self.__inventario.__str__() # bucle for para
                                        # retornar cada objeto


inventario = Inventario()

tuberia1 = Tuberia(0,10)
tuberia2 = Tuberia(1,20)
inventario.__add__(tuberia1)
inventario.__add__(tuberia2)

print (inventario)