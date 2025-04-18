"""
Yeni data tip: list()
Dəyər [] əhatə olunur və elemntlər bir birilə , -lə ayrılır.

Məs.:
empty_list = []
my_int_list = [12, 15, 105, 0, -5]
my_str_list = ["salam", "hello", "hallo"]

my_mixed_list = [15, "hello", True]
"""
my_mixed_list = [12, 15, 1556, 15, -5.14, 323434, 34344]

"""
Hər hansı elementi onun indeksi ilə əldə edə bilərik. 
Məs.: print(my_mixed_list[1])

Həm də istənilən indeksdəki dəyəri dəyişmək mümkündür.
Məs.: my_str_list[1] = "salam"
"""
print(my_mixed_list[1])
print(my_mixed_list[0])
print(my_mixed_list[-1])
print(my_mixed_list[0:3])

print("------------------------")

"""
count()
append()
extend()
pop()                   -> __index attribute-u -> pop(3)
sort()                  -> reverse attribute-u -> sort(reverse=True)


Pythonda listlər üçün bəzi vacib built-in funksiyalar:
del my_mixed_list[3]
len()
max()
min()
sum()
"""
print(len(my_mixed_list))
print(max(my_mixed_list))
print(min(my_mixed_list))
print(sum(my_mixed_list))
# my_mixed_list.append(1000)
print(my_mixed_list)
print("------------------------")

"""
FOR DÖNGÜSÜ:

for <döngü elementi> in <döngü listi, ardıcıllığı>
    <kod bloku>

# step dəyəri həm də mənfi ədəd ola bilər, lakin yalnız o halda ki, start stop-dan böyükdür.
for i in range(0, 10, 2):  # start, stop, step
    print(i)
    
start default: 0
stop mütləq təyin olunmalıdır
step default: 1
"""
"""
0   -- index, value
2   -- index, value
(2, 4)   -- index, value
(3, 6)   -- index, value
(4, 8)   -- index, value
"""

"""
Listlərdə for döngüsü

my_list = ['a', 'b', 'c', 'd']
for item in my_list:
    print(item)
"""


my_list = [12, 15, 1556, 15, -5.14, 323434, 34344]
for element in my_list:
    print(element)
    if element == 15:
        pass
    print("swaqda")

for element in range(15, 0, -1):
    print(element)

my_str = "Salam"

for char in my_str:
    print(char)

"""
string üçün for döngüsü

my_str = 'hello'
for char in my_str:
    print(char)
"""
