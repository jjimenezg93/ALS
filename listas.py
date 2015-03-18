__author__ = 'jjgonzalez'

l1 = []
l2 = list()

l1 += [1, 2 ,3]
l2.append(4)

print(l1)
print(l2)

del l1[2]
del l2[-1]

print(l1)
print(l2)

print(l1[0])
#print(l2[0])

print(l1[0:-1]) # = print(l1[:])

for i in l1:
    print(i)

print("hola"[:-2])

def inversa(l):
    """Calcula la inversa de una lista

    :param l: la lista de la que calculamos la inversa
    :return: inversa, como una lista
    """
    toret = []

    for i in l:
        toret = [i] + toret
    return toret

l3 = [1,2,3]
print(inversa(l3))


for i, x in enumerate(l1):
    print("#{0}: {1}".format(i,x))


def es_anagrama(s1, s2):
    """ comprueba que ambas palabras contienen las mismas letras

    :param s1: La primera cadena
    :param s2: La segunda cadena
    :return: True si son anagramas. False en otro caso
    """
    for i in s1:
        toret = True
        if s1.count(i) != s2.count(i):
            toret = False
            break
    return toret

def es_anagrama2(s1, s2):
    """ comprueba que ambas palabras contienen las mismas letras.

    :param s1: La primera cadena
    :param s2: La segunda cadena
    :return: True si son anagramas. False en otro caso
    """
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()
    return s1 == s2

def fibonacci(v):
    """

    :param v: Numero de valores de la lista
    :return: lista con v numeros de la sucesion de Fibonacci
    """
    toret = list()
    for i in range(v):
        if i<2:
            toret.append(1)
        else:
            toret.append(toret[i-2] + toret[i-1])

    return toret

print (es_anagrama("anan", "nana"))
print (es_anagrama("ana", "nana"))

print (es_anagrama2("anan", "nana"))
print (es_anagrama2("ana", "nana"))

print (fibonacci(8))