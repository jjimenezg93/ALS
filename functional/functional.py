__author__ = 'Julián'

def ClassicDouble(x):
    return x * 2
# same than
double = lambda x: x * 2
appleOrorange = lambda s: 5 if s == "apple" else 6

fact = lambda x: 1 if x == 1 \
    else x * fact(x-1)

print(double(4))
print(ClassicDouble(4))
print(appleOrorange("apple"))
print(appleOrorange("orange"))
print(fact(5))


##### SIMULATING LISP #####

# car(l): returns {0}
# cdr(l): returns sublist {1:}
# SO, if l = {1, 2, 3}
# then car(l) = 1, cdr(l) = {2,3}

car = lambda l: None if l == None or l == [] \
    else l[0]

cdr = lambda l: [] if l== None or l == [] \
    else l[1:]

listPrint = lambda l: "" if l == [] or l == None \
    else car(l) if cdr(l) == [] \
    else str(car(l)) + ", " + str(listPrint(cdr(l)))

l = [1, 2, 3, 4, 5]
l2 = []
print(listPrint(l))
print(listPrint(l2))



fibo = lambda n: \
    0 if n <= 1 else \
    1 if n == 2 else \
    fibo(n-1) + fibo(n-2)

reverse = lambda l: \
    [] if l == None or l == [] \
    else reverse(cdr(l)) + [car(l)]

fibonacci = lambda n: \
    [] if n <= 0 \
    else [0] if n == 1 \
    else [0, 1] if n == 2 \
    else fibonacci(n-1) + [fibo(n-1) + fibo(n-2)]
    # else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]
    # else fibonacci(n-1) + [car(reverse(fibonacci(n-1))) + car(cdr(reverse(fibonacci(n-1))))}

# filter(l, f): returns elements of l which are true for f
# map(l, f): returns elements of l applied to f
# reduce(l, f): returns a value of applying f to all l elements

filter = lambda l, f: \
    [] if l == None or l == [] \
    else [car(l)] + filter(cdr(l), f) if f(car(l)) \
    else filter(cdr(l), f)

map = lambda l, f: \
    [] if l == None or l == [] \
    else [f(car(l))] + map(cdr(l), f)

reduce = lambda l, f: \
    car(l) if cdr(l) == [] \
    else f(car(l), reduce(cdr(l), f))


l = [1, 2, 3, 4, 5]

print(fibo(6))
print(fibonacci(5))

print(filter(l, lambda x: x % 2 == 0))
print(map(l, lambda x: x * 2))
print(reduce(l, lambda x, y: x + y))