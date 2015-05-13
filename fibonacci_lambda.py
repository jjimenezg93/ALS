__author__ = 'Oscar'

car = lambda l :  Noneif l == None or l == [] else l[0]
cdr = lambda l : [] if l == None or l == [] else\
    [] if len(l) == 1 else \
    l[1:]


#recorrer una lista para imprimirala
to_str = lambda l : "" if l == [] or l == None else\
    car(l) if cdr(l) == [] else \
    str(car(l))+ str(to_str(cdr(l)))


fibo = lambda n : 0 if n <= 1 else \
    1 if n == 2 else \
    fibo(n-1)+fibo(n-2)

reverse = lambda l : \
    [] if l == None or l == [] else \
    reverse(cdr(l))+[car(l)]

fibonacci = lambda n : \
    [] if n <= 0 else \
    [0] if n == 1 else \
    [0,1] if n == 2 else \
    fibonacci(n-1)+[fibo(n)]

#filter devuelve los elementpos de l para los que f devuelve true
#map devuelve l con sus elementos aplicados a f
#reduce devuelve un valor un resultante de aplicar f a l

filter = lambda l, f : \
    [] if l == None or l == []  else \
    [car(l)] + filter(cdr(l),f) if (f(car(l))) else \
    filter (cdr(l),f)

map = lambda l,f : \
    [] if l == None or l == [] else \
    [f(car(l))]+ map(cdr(l,f))

reduce = lambda l,f : \
    car(l) if cdr(l) == [] else\
    f(car(l),reduce(cdr(l),f))



print(fibo(5))
print(fibonacci(5))


l = [1,2,3]
print(to_str(l))
print(to_str([]))