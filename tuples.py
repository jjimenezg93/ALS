__author__ = 'Julián'

tupla_vacia = tuple()
t0 = (1,)
t1 = (1,2,3)

#t1[0] = 9 ##SON INMUTABLES, NO SE PUEDEN MODIFICAR

print(len(t1))
print(min(t1))
print(max(t1))
print(t1[0])
print(t1[-1])
print(t1[1:3])
print(t0 + t1)