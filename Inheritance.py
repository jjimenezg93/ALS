__author__ = 'Julián'

class Persona:
    def __init__(self, n):
        self.__nombre = n

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return self.nombre

class Empleado(Persona):
    def __init__(self, n, e):
        super().__init__(n)
        #Persona.__init__(n)
        self.__empresa = e

    @property
    def empresa(self):
        return self.__empresa

    def __str__(self):
        return "{0}, {1}".format(super().__str__(), self.empresa)

e = Empleado("Juli", "Aqui SA")
print (e)