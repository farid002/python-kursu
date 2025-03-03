"""
Tez-tez istifadə olunan vacib Built-In Python funksiyaları
"""
"""
len()
any()
all()
map()
filter()
enumerate()
"""
# print(all([True, True, True, True, True, True, False]))
# from math import factorial


def divisible_by_2(x):
    if x % 2 == 0:
        return True
    return False

my_list = [1, 2, 4, 5, 3]
# print(all([number%4==0 for number in my_list]))
# print(any([number%4==0 for number in my_list]))
print(my_list)
# factorial_list = list(map(factorial, my_list))
# print(factorial_list)
print(list(filter(divisible_by_2, my_list)))



"""
sum()
max()
min()
sorted()
reversed()
"""
print("my max", max(my_list))
print("my min", min(my_list))
print("my sum", sum(my_list))
print("my sorted", sorted(my_list))
print("my reversed", list(reversed(my_list)))

sorted_list = sorted(my_list)

"""
type()
isinstance()
id()
"""
print("===================")
print(type("Hello"))
print(type(my_list))
print(type(False))

print(isinstance(sorted_list, (bool, str, int)))


"""
print()
input()
"""

"""
int()
float()
str()
list()
dict()
tuple()
bool()
"""


"""
import
as
*
from
venv
requirements.txt
"""
from math import factorial
from ders10.oghuz import factorial
from ders10 import oghuz

print(factorial(5))
