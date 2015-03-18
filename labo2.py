__author__ = 'jjgonzalez'

"""
Labo 2 - Estructuras de datos
"""

# Ejercicio 1

import math

def media(l):
    return sum(l)/len(l)

def mayor(l):
    mayor = l[0]
    for i in l:
        if i > mayor:
            mayor = i
    return mayor

def menor(l):
    menor = l[0]
    for i in l:
        if i < menor:
            menor = i
    return menor

def desv_tip(l):
    total = 0
    for i in range(0,len(l)):
        value = l[i]
        value = value - media(l)
        value = value**2
        total = total + value
    total = total/float(len(l))
    return math.sqrt(total)

def calculos(l):
    print("Media = {0}".format(media(l)))
    print("Mayor = {0}".format(mayor(l)))
    print("Menor = {0}".format(menor(l)))
    print("Desv. Tipica = {0}".format(desv_tip(l)))
"""
numeros = list()
flag = 1

while flag != 0:
    entrada = input("Introduzca un numero: ")
    entrada = int(entrada)
    if entrada != 0:
        numeros.append(entrada)
    else:
        calculos(numeros)
        flag = entrada
"""
# Ejercicio 2

def calcular(l):
    if l[0] == "+":
        return calcular2(l[1:], "+")
    elif l[0] == "-":
        return int(l[1]) - calcular(l[2:])
    elif l[0] == "*":
        return int(l[1]) * calcular(l[2:])
    elif l[0] == "/":
        return int(l[1]) / calcular(l[2:])
    else:
        return int(l[0])

def calcular2(l, op):
    if l[0] == "+":
        return 
    elif l[0].isDigit():


flag = 1

while flag != 0:
    entrada = input("Introduzca una expresion: ")
    print(calcular(entrada.split()))