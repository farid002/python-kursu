"""
Tək sətirdə iç-içə döngüdə list elementləri üzərində əməliyyat (nested loop list comprehension)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in my_list for item in row]
print(flattened)
"""

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(my_list[2][2])

duzleshmish_list = [item for row in my_list for item in row]
# print(duzleshmish_list)

"""
Döngülərdə else (could not found misalları)
"""

for number in duzleshmish_list:
    if number == 100:
        break
    print(number)
else:
    print("Tapilmadi")


index = 0

while index < len(duzleshmish_list):
    print(duzleshmish_list[index])
    if duzleshmish_list[index] == 15:
        break
    index = index + 1
else:
    print("Tapilmadi")

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