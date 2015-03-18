# coding=utf-8
__author__ = 'Julián'

#POO

import math
import numbers

class Punto:
    def __init__(self, x, y):
        self.x = x # si utilizamos self.__x, creamos aquí la propiedad
        self.y = y

    @staticmethod   # metodo estatico, no necesita self
    def get_org():
        return (0,0)

    @property   # método especial que va a ser llamado cuando se intente acceder a x, EQUIVALE AL GETTER
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

# def get_x(self)
# def set_x(self, value)
# x = property(get_x, set_x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __eq__(self, other):    # se llama si se intenta utilizar el operador ==
        if not(isinstance(other, Punto)):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):    # se llama si se intenta utilizar el operador !=, también neq y neg
        if not(isinstance(other, Punto)):
            return True
        return self.x != other.x or self.y != other.y

    def modulo(self):
        return math.sqrt(self.x ** 2 + self.y **2)

    def __gt__(self, other):    # mayor
        if not(isinstance(other, Punto)):
            return False
        return self.modulo() > other.modulo()

    def __lt__(self, other):    # menor
        if not(isinstance(other, Punto)):
            return False
        return self.modulo() < other.modulo()

    def __ge__(self, other):    # mayor o igual
        if not(isinstance(other, Punto)):
            return False
        return self.modulo() >= other.modulo()

    def __le__(self, other):    # menor o igual
        if not(isinstance(other, Punto)):
            return False
        return self.modulo() <= other.modulo()

    def __add__(self, other):   # suma
        if not(isinstance(other, Punto)):
            #return -1   # lo correcto es lanzar una excepcion
            raise TypeError("Punto + ?")
        return Punto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # resta
        if not(isinstance(other, Punto)):
            #return -1   # lo correcto es lanzar una excepcion
            raise TypeError("Punto - ?")
        return Punto(self.x - other.x, self.y - other.y)

    def __mul__(self, k):   # multiplicacion * K
        if not(isinstance(k, numbers.Number)):
            #return -1   # lo correcto es lanzar una excepcion
            raise TypeError("Punto * ?")
        return Punto(self.x * k, self.y * k)

    def __floordiv__(self, k):   # division entera
        if not(isinstance(k, numbers.Number)):
            #return -1   # lo correcto es lanzar una excepcion
            raise TypeError("Punto // ?")
        return Punto(self.x // k, self.y // k)

    def __truediv__(self, k):   # division normal
        if not(isinstance(k, numbers.Number)):
            #return -1   # lo correcto es lanzar una excepcion
            raise TypeError("Punto / ?")
        return Punto(self.x / k, self.y / k)

    def __str__(self):  # EQUIVALE A ToString
        return "({0}, {1})".format(self.x, self.y)

class Linea:
    def __init__(self, x1, y1, x2, y2):
        if (isinstance(x1, Punto) and isinstance(y1, Punto)):   # Si x1 e y1
            self.__p1 = x1
            self.__p2 = y1
        else:
            self.__p1 = Punto(x1, y1)
            self.__p2 = Punto(x2, y2)

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    def __str__(self):
        return "({0}, {1})".format(self.p1, self.p2)

p1 = Punto(1,2)
p2 = Punto(3,4)
p3 = Punto(12,15)

print (p1)
print (dir(p1)) #devuelve una lista con los miembros del objeto

print ("{0} == {1}?? == {2}".format(p1, p2, p1==p2))
print ("{0} == {1}?? == {2}".format(p1, p1, p1==p1))
print ("{0} > {1}?? == {2}".format(p1, p2, p1 > p2))
print ("{0} < {1}?? == {2}".format(p1, p2, p1 < p2))
print ("{0} >= {1}?? == {2}".format(p1, p2, p1 >= p2))
print ("{0} <= {1}?? == {2}".format(p1, p2, p1 <= p2))
print ("{0} + {1}?? == {2}".format(p1, p2, p1 + p2))
print ("{0} - {1}?? == {2}".format(p1, p2, p1 - p2))
#print ("{0} - 2 EXCEPTION?? == {2}".format(p1, p2, p1 - 2))

k = 3
print ("{0} * {1}?? == {2}".format(p1, k, p1 * k))
print ("{0} // {1}?? == {2}".format(p3, k, p3 // k))
print ("{0} / {1}?? == {2}".format(p3, k, p3 / k))

## lineas
linea1 = Linea(1,2,3,4)
print (linea1)

linea2 = Linea((1,2), (3,4), None, None)
print (linea2)

#### EXCEPCIONES ####
def main():
    try:
        p1 = Punto(1, 2)
        assert (p1 != None)     # assert lanza la excepcion "AssertionError" cuando no se cumple la condicion
        print (p1 + "iafshoi")
    except TypeError as e:
        print("Error de tipos: " + str(e))
    except:
        print("[PANIC] Error inesperado")

main()