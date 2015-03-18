__author__ = 'Julián'

## EJ 1

def es_palindromo(s):
    cadena = s

    x = 0
    y = -1
    toret = True
    for i in s:
        if cadena[x] == cadena[y]:
            x += 1
            y -= 1
        else:
            toret = False
    return toret

print(es_palindromo("radar"))

## EJ 2


def histograma(l):
    lista = l
    toret = {}
    for i in l:
        if toret.get(i) == None:
            toret[i] = "*"
        elif len(toret[i]) < 11:
            toret[i] += "*"
    print(toret)

histograma([1, 2, 3, 2, 2,2,2,2,2,2,2,2,2,2,2,2])

## EJ 3

def inversa(l):
    toret = list()
    for i in l:
        toret.insert(0,i)
    print(toret)

inversa([1,2,3])

## EJ 4

class Punto():
    def __init__(self, x ,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

class Linea():
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    def __str__(self):
        return "({0}-{1})".format(self.p1,self.p2)

class Poligono():
    def __init__(self, puntos):
        self.__lineas = list()
        x=-1
        for i in puntos:
            linea = Linea(puntos[x],puntos[x+1])
            x += 1
            self.__lineas.append(linea)

    @property
    def lineas(self):
        return self.__lineas

    def __str__(self):
        toret=""
        for i in self.lineas:
            toret += str(i)
        return toret

p1 = Punto(1,2)
p2 = Punto(3,4)
p3 = Punto(4,5)
p4 = Punto(5,6)
l1 = Linea(p1,p2)

print(p1)
print(l1)

poligono = Poligono([p1,p2,p3,p4])
print(poligono)

class Estudiante():
    def __init__(self, dni, nombre, email):
        self.__dni = dni
        self.__nombre = nombre
        self.__email = email

    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    def __str__(self):
        return "{0}, con DNI {1}, email {2}".format(
            self.dni, self.nombre, self.email
        )

class EstudianteNormal(Estudiante):
    def __init__(self, dni, nombre, email, provincia):
        super().__init__(dni, nombre, email)
        self.__provincia = provincia

    @property
    def provincia(self):
        return self.__provincia

    def __str__(self):
        return super().__str__() + " y provincia {0}".format(
            self.provincia
        )

class EstudianteErasmus(Estudiante):
    def __init__(self, dni, nombre, email, pais):
        super().__init__(dni, nombre, email)
        self.__pais = pais

    @property
    def pais(self):
        return self.__pais

    def __str__(self):
        return super().__str__() + " y pais {0}".format(
            self.pais
        )


normal = EstudianteNormal("54534235", "Pepe", "pepe@pepe", "Ourense")
erasmus = EstudianteErasmus("54534235", "Manolo", "manolo@manolo", "Ourense")

print (normal)
print (erasmus)