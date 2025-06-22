#  oop 1 type encapsulation

# from traceback import print_tb


# class Pesron:
#     def __init__(self,name, age , id):
#         self.name = name,
#         self.age = age,
#         self.id = id
    
#     def student (self):
#         return self.name
#     def Agestudent(self):
#         return self.age
#     def Idstudent(self):
#         return self.id
    
# s1 = Pesron("Nitu", 21, "sopu")
# print(s1.student())
# print(s1.Agestudent())
# print(s1.Idstudent())

# Abstraction 

# from abc import abstractmethod


# class Person:
#     @abstractmethod
#     def make_sound(self):
#         pass
    
# class Animal(Person):
#     def make_sound(self):
#         return "Bark"
# s1 = Person()
# print(s1.make_sound())

from abc import abstractmethod



class Animal:
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def make_sound(self):
        return "Myau"
class rat(Animal):
    def make_sound(self):
        return "Chichi"   
    
Animals = [Dog(), Cat() ,rat()]
for Animal in Animals:
    print(Animal.make_sound())



# 3 Inheritance

class Animal:
    def eat(self):
        print("animals are eat food ")
    
class eog(Animal):
    def makesound(self):
        print("bark")

s1 = eog()
s1.eat()
s1.makesound()        

# Polymorphism

class wog:
    def eeat(self):
        print("this eat food")

class iat:
    def eeat(self):
        print("this eat food")

for animal in (wog(), iat()):
    print(animal.eeat())


# try add except

