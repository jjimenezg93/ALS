__author__ = 'Julián'

class Worker:
    def __init__(self, n, s):
        self.__nombre = n
        self.__salary = s

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        self.__salary = s

        if (s >= 3000 ):
            self.__class__ = Boss
        else:
            self.__class__ = Currito

    def __str__(self):
        return "{0}: {1}".format(self.nombre,self.salary)

class Currito(Worker):
    def __init__(self, n, s):
        super().__init__(n, s)

    def __str__(self):
        return "Currito " + super().__str__()

class Boss(Worker):
    def __init__(self, n, s):
        super().__init__(n, s)

    def __str__(self):
        return "Boss " + super().__str__()

c1 = Currito("Pepe", 1500)
c2 = Boss("Manolo", 1500)
print(c1)
print(c2)

c1.salary = 4500
print(c1)
print(c2)