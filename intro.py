# Intro Python

def factorial(n):
    """
    Calcula RECURSIVAMENTE el factorial de un numero.
    """
    # entre """ """ se puede crear la documentacion del help(factorial)
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def factorial2(n):
    """
    Calcula el factorial de un numero.
    """
    toret = 1
    while n > 1:
        toret *= n
        # --n NO FUNCIONA
        n -= 1
    else:
        print("WHILE TERMINADO")
    return toret

def factorial3(n):
    """
    Calcula ITERATIVAMENTE el factorial de un numero.
    """
    toret = 1
    for i in range(1, n + 1):
        toret *= i
    else:
        print("FOR TERMINADO")
    return toret

print ("Hola, mundo!")

print ( """Hola,

mundo!""") # mantiene literalmente los espacios

print("Clase de {0}, es la {1:02} clase.".format("ALS",1)) # con {1:02} hacemos que añada 0s para 2 posiciones

entrada = input("Dame tu nombre: ")
print("Tu nombre es: " + entrada)

entrada = input("Dame tu edad: ")
edad = int(entrada)
print("Tu edad es: {0}".format(edad))

pi = float(input("Escribe PI: "))
print("Según tú, PI es: {0}".format(pi))

print(factorial(7))
print(factorial2(7))
print(factorial3(7))