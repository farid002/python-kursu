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

"""
sum()
max()
min()
sorted()
reversed()
"""

"""
type()
isinstance()
id()
"""

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

a = input("Kodunuzu yazin:\n")

def parol():
    kod0 = False
    kod1 = False
    kod2 = False
    kod3 = False
    if len(a) >= 8:
        kod0 = True
    for herf in a:
        if herf.isupper():
            kod1 = True
            break
    for herf in a:
        if herf.islower():
            kod2 = True
            break
    for herf in a:
        if herf.isdigit():
            kod3 = True
            break
    return kod0, kod1, kod2, kod3

if __name__ == '__main__':
    k0, k1, k2, k3 = parol()
    if k0 and k1 and k2 and k3:
        print("Kodunuz gucludur.".isalnum())
    else:
        print("Kodunuz guclu deyil.")
