## EJERCICIO 1

meses = {"Ene": "01", "Feb": "02", "Mar": "03", "Abr": "04"}

def fechas(s):
    copia_original = s.strip().split()
    dia = copia_original[0]
    mes = meses[copia_original[1]]
    anho = copia_original[2]

    return anho + "-" + mes + "-" + dia

print(fechas("12 Feb 2015"))

## EJERCICIO 3
terminar = False
posibles_opciones = [1 , 2 , 3, 0]
datos = dict()
def menu():
    print("Introduzca la opcion ")
    print("1) Introducir ")
    print("2) Borrar ")
    print("3) Buscar ")
    print("4) Listado ")
    print("q) Salir ")
    op = input("")
    return op
def get_nombre():
    nombre = input("Nombre: ")
    if nombre != None:
        return nombre
    else:
        return None
def introducir():
    nombre = get_nombre()
    email = input("Email: ")
    if datos.get(nombre) == None:
        datos[nombre] = email
    else:
        datos[nombre].append(email)
def borrar():
    nombre = get_nombre()
    if datos.get(nombre) == None:
        print("")
        print ("No existe este nombre")
        print("")
    else:
        print("")
        datos.__delitem__(nombre)
        print("")
def buscar():
    nombre = get_nombre()
    if datos.get(nombre) == None:
        print("")
        print ("No existe este nombre")
        print("")
    else:
        print("Datos: {0}".format(datos[nombre]))
        print("")
def listado():
        print(datos)
def quitar():
    global terminar
    terminar = True
dict_switch = {"1":introducir, "2":borrar, "3":buscar, "4":listado, "q":quitar}
while(not terminar):
    opcion = menu()
    dict_switch[opcion]()