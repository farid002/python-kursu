from abc import ABC, abstractmethod


class Animal:
    def make_sound(self):
        return "Making sound"

class Dog(Animal):
    pass

class Cat(Animal):
    def make_sound(self):
        return "Miyov!"

class Rat:
    pass

dog = Dog()
cat = Cat()
rat = Rat()

print(dog.make_sound())
print(cat.make_sound())
print(rat.make_sound())