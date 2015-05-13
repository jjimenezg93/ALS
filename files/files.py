import os
import pickle
import json
import sys
# args = sys.argv

__author__ = 'Julián'

# f = open("name", "opening_mode") - r, w, b, t, a, U

class Point():
    def __init__(self, a, b):
        self.__x = a
        self.__y = b

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


def create_file(name, data):
    # f = open(name, "wt")
    # f.write(data)
    # f.close()
    with open(name, "wt") as f:
        f.write(data)

def read_file(name):
    #toret = ""
    with open(name, "rU") as f:
        #toret = f.readlines()
        for line in f:
            print(line)
    #return toret

def count_words(name):
    toret = 0
    with open(name, "rU") as f:
        for line in f:
            toret += len(line.split())
        return toret

if os.path.isfile("data.txt"):
    create_file("data.txt", "hi Python!! how are you? you you")

read_file("data.txt")
print(count_words("data.txt"))

# Creating objects
p1 = Point(1,2)
p2 = Point(2,3)
l = [p1, p2]

def demo_pickle():
    # Saving objects to binary
    f = open("data.bin", "wb")
    pickle.dump(l, f)
    f.close()

    # Getting objects from binary
    del l[0]
    del l[0]
    f = open("data.bin", "rb")
    l = pickle.load(f)
    f.close()

    print(l)
    print(l[0])
    print(l[1])

# We should make a methor to serialize Point object before passing it to JSON
def demo_json():
    # Saving objects to binary
    f = open("data.json", "wt")
    json.dump(l, f)
    f.close()

    # Getting objects from binary
    del l[0]
    del l[0]
    f = open("data.json", "rb")
    l = json.load(f)
    f.close()

    print(l)
    print(l[0])
    print(l[1])

# demo_json()

l = [1, 2]
strL = json.dumps(l)
print(strL)
print(json.loads(strL))

d = {"value": 1}
strD = json.dumps(d)
print(strD)
print(json.loads(strD))

def count_ocurrences(name):
    toret = {}
    with open(name, "rU") as f:
        for line in f:
            res = line.split()
            line.
            for i in res:
                if toret.__contains__(i.lower()):
                    toret[i.lower()] += 1
                else:
                    toret[i.lower()] = 1
    return toret

print(count_ocurrences("data.txt"))