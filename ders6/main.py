"""
enumerate()
"""
"""
alphabets = ["A", "B", "C", "D", "E", "F"]

for index, alphabet in enumerate(alphabets):
    if alphabet == "C":
        print(index)
"""
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
my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    squares.append(my_number**2)


squares = sum([my_number**2 for my_number in [1,3,4,5,6]])
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
print([my_number**2 if my_number % 2 == 0 else -1 for my_number in [1,2,3,4,5,6]])

my_list = []
for my_number in [1,2,3,4,5,6]:
    if my_number % 2 == 0:
        my_list.append(my_number**2)
    else:
        my_list.append(-1)
print(my_list)
"""

"""
Tək sətirdə iç-içə döngüdə list elementləri üzərində əməliyyat (nested loop list comprehension)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in my_list for item in row]
print(flattened)
"""

"""
Döngülərdə else (could not found misalları)
"""

"""
Pseudocode
"""

"""
Flowchart

Dairə - start, end
Romb - şərt
Kvadrat - proses
Oxlar - axın yönü
"""