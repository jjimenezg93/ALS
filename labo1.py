# Laboratorio 1 - ALS
# Julián Jiménez González

###### 1 ######

print ("¡Hola, Mundo!")

###### 2 ######

entrada = input("Dime tu nombre: ")
print("Hola, {0} :)".format(entrada))

###### 3 ######

def pedir_Nombre():
    nombre = input("Dime tu nombre: ")
    return nombre

def mostrar_Nombre(n):
    print("Hola, {0} :):)".format(n))

mostrar_Nombre(pedir_Nombre())

###### 4 ######

def fmtCoordenadas():
    x = int(input("Introduce numero 1: "))
    y = int(input("Introduce numero 2: "))
    
    print("({0},{1})".format(x,y))
    
def fmtCoordenadas2():
    x = int(input("Introduce numero 1: "))
    y = int(input("Introduce numero 2: "))
    
    print("(" + str(x) + "," + str(y) + ")")

fmtCoordenadas()
fmtCoordenadas2()

###### 5 ######

def calcular_Operacion(x,y,op):
    if op == '+':
        return x + y
    elif op == '*':
        return x * y
    elif op == '/':
        return x/y
    elif op == '^':
        return x**y

def pedir_Datos():
    x = int(input("Introduce numero 1: "))
    y = int(input("Introduce numero 2: "))
    op = input("Introduce operacion: ")
    print(calcular_Operacion(x,y,op))

pedir_Datos()