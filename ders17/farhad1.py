from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Hav hav!")

class Cat(Animal):
    def make_sound(self):
        print("Miyov!")


dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()