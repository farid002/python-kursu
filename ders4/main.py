"""
WHILE DÖNGÜSÜ


i = 10

while i > 2:
    i = i - 1
    print("Hi")

print("End")
"""

i = 10

while i >= 2:
    print(i)
    i = i - 1

"""
Döngülərdə:
    break, continue, pass
"""

my_list = ["Salam", "Sagol", "Necesen","Baku", "Ganja", "Frankfurt"]

i = -1
while i < len(my_list) - 1:
    i = i + 1
    if my_list[i] == "Sagol":
        continue
    print(my_list[i])


""" 
enumerate()
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [my_number**2 for my_number in my_list if my_number%2 == 0]
print(squares)


"""
Tək sətirdə list elementləri üzərində əməliyyat (list comprehension)

my_list = [1, 2, 3]
squares = [my_number**2 for my_number in my_list]
print(squares)


klassik metod:

my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    squares.append(my_number**2)
print(squares)
"""


"""
Tək və ya cütlüyü yoxlayan proqram

my_list = [1, 2, 3, 4, 5, 6]
result = ['Cüt' if my_number % 2 == 0 else 'Tək' for my_number in my_list]
print(result)

klassik metodla:
my_list = [1, 2, 3, 4, 5, 6]
result = []
for my_number in my_list:
    if my_number % 2 == 0:
        result.append("Cüt")
    else:
        result.append("Tək")
print(result)
"""

"""
Tək sətirdə iç-içə döngüdə list elementləri üzərində əməliyyat (nested loop list comprehension)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in my_list for item in row]
print(flattened)
"""

my_list = [[1, 5, 3], [4, 5, 6], [7, 4, 9]]
flattened = (item for row in my_list for item in row)

for item in flattened:
    print(item)
    break
else:
    print("salam")

"""
Döngülərdə else
Tek qayda: Loop icinde break etdise, else'e girmeyecek. Eks halda (break ishlense ancaq break'e girmese bele) else'e girecek
"""
