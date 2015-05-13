__author__ = 'Julián'

import os
import pickle
import sys

class Person():
    def __init__(self, n, e):
        self.__name = n
        self.__email = e

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def __str__(self):
        return "---- \n" \
               "Name: {0} \n" \
               "Email: {1} \n" \
               "----".format(self.name, self.email)

p1 = Person("Pepe", "Pepe@pepe.com")
print(p1)



def insert_contact():
    print("Insert contact's name: ")
    name = input()
    print("Insert contact's email: ")
    email = input()


def list_contacts():
    pass

def delete_contact():
    pass

options = {"1": insert_contact, "2": list_contacts, "3": delete_contact}

def menu():
    print("1. Insert \n"
          "2. List \n"
          "3. Delete \n"
          "4. Exit \n")
    option = input()
    return option

# main
while opt != 4:
    opt = menu()
    options[opt]()