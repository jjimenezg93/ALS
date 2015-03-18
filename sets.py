__author__ = 'Julián'

# Parecidos a listas pero donde no hay repeticion de elementos

c0 = set()
c1 = set([1,1,2,2,3,3])
c2 = set((3,4,5))

print(c0)
print(c1)
print(c2)

print(c0 | c1)
print(c0 & c1)
print(c1 & c2)
print(c1 - c2)