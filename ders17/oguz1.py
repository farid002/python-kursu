"""
Animal adlı abstrakt sinif yaradın və abstrakt metod make_sound() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Dog sinfi make_sound() metodunu "Hav-hav!" qaytaracaq şəkildə implement etsin.
    2. Cat sinfi make_sound() metodunu "Miyov!" qaytaracaq şəkildə implement etsin.

Dog və Cat siniflərindən obyektler yaradın və make_sound() metodunu çağırın.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Hav-Hav")
class Cat(Animal):
    def make_sound(self):
        print("Miow")
dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()