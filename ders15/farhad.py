class Animal:
    def __init__(self, name, age, cins):
        self.name = name
        self.age = age
        self.cins = cins

    def make_noise(self):
        print("Bu heyvan səs çıxarır")

class Dog(Animal):
    pass

class Cat(Animal):
    def make_noise(self):
        print("Miyov-miyov!")

my_dog = Dog("Rex", 3, "dishi")
my_cat = Cat("Ozzy", 2, "erkek")
my_dog.make_noise()
my_cat.make_noise()