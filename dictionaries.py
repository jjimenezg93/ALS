#dicts clase 1

temperaturas = { "Ourense": 5, "Vigo": 12 }
temperaturas[ "Lugo" ] = 2

print(temperaturas["Ourense"]) #lanza excepcion
print(temperaturas.get("Ourense"))

dict1 = {}
dict1 = dict()

for k,v in temperaturas.items():
    print( "Para {0}: {1}º ".format(k,v))

for k in temperaturas.keys():
    print( "Hay temperatura para: {0}".format(k))

for v in temperaturas.values():
    print( "Temperatura almacenada de {0}".format(v))

def fn1():
    print("1")

def fn2():
    print("2")

dict_switch = {1:fn1, 2:fn2}
dict_switch[1]()
dict_switch[2]()

# str.strip() ## elimina espacios al principio y al final
# str.split() ## devuelve un array resultante de dividir la cadena por un caracter

###### Crea una función wc(s), que cuente las palabras en la cadena que se le pasa. La función devolverá un dict con
###### Key = palabra, Value = ocurrencias

def wc(s):
    palabras = s.strip().split()
    toret = {}
    for k in palabras:
        if toret.get(k) == None:
            toret[k] = 1
        else:
            toret[k] += 1
    return toret


print(wc("hola que tal como que que estas"))

###### Crea una función eliminar_repetidos(l), a la que le pasamos una lista y devuelve
###### una nueva lista con los elementos que hay en la lista original pero sin repetir

##################### NO FUNCIONA ################
# list.index(i) devuelve la posicion, no si esta o no

def elimina_repetidos(l):
    toret = list()
    for k in l:
        if toret.__contains__(k) == False:
            toret.append(k)
    return toret

l = [1,1,2,3]
print("Elimina repetidos")
print(l)
print(elimina_repetidos(l))

###### Crea una función es_anagrama(s1,s2), que devuelve true si s1 es anagrama de s2

def es_anagrama(s1,s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()

    def get_dict(s):
        toret = {}
        for i in s:
            if toret.get(i) == None:
                toret[i] = 1
            else:
                toret[i] += 1
        return toret
    if (len(s1) == len(s2)):
        return get_dict(s1) == get_dict(s2)
    else:
        return False


print(es_anagrama("naa","ana")) #true
print(es_anagrama("nana","ana")) #false