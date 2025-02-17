"""
TUPLE
- Dəyişdirilə bilməyən (immutable)
- Sirali
koordinatlar (x, y, z), doğum tarixi ve s.
"""
my_tuple = (1, 2, 3)
my_list = [1, 2, 3, 5, 3, 2]

my_list[0] = 5

coordinate_x = 50
coordinate_y = 45

coordinate = (50, 45)
birthday = (1999, 5, 12)

for index, value in enumerate(my_list):
    print("")


my_list = [(0, 1), (4, 5), (7, 8)]
for something in enumerate(my_list):
    print(something)

"""
SET
- Unikal (tekrarlanmayan deyerler)
- Deyisdirile bilen (mutable)
Hesablama emeliyyatlari: kesisme, birlesme
"""
my_set = {1, 2, 3, 4}
my_set_2 = {1, 2, 5, 8}

# my_set.add(6)
# my_set.add(6)
# my_set.remove(3)
print("Union:", my_set.union(my_set_2))
print("Intersection:", my_set.intersection(my_set_2))
print("Intersection:", my_set.intersection(my_set_2))
print("Diff. my_set - my_set_2:", my_set.difference(my_set_2))
print("Diff. my_set_2 - my_set:", my_set_2.difference(my_set))
print("Diff. my_set_2 - my_set:", my_set_2.symmetric_difference(my_set))
print("Either A or B:", my_set.union(my_set_2).difference(my_set.intersection(my_set_2)))
print("Diff. my_set_2 - my_set:", my_set_2.symmetric_difference(my_set))
print("Is set2 subset of set", my_set_2.issubset(my_set))
print("Is set superset of set2", my_set.issuperset(my_set_2))
my_set.remove(1)
print("remove 1", my_set)
print("Disjoint", my_set.isdisjoint(my_set_2))
my_set.intersection_update(my_set_2)
print("Inter Update", my_set)
my_list = [3,5,6,5,65,46,3,52,34,2,34,2,4,25,35,3,6,4,76,4567,3,3245,23,4,3]
print("????????????")
print(set(my_list))


print("=========================")
print(my_list)
print(set(my_list))

for item in my_set:
    print(item)

"""
DICT
- Genis istifade yerleri
- Boyuk datalarda suretli proses (acarlarla indeks)
- Deyisdirile bilen (mutable)
"""
print("==========================")
my_dict = {
    "a": [1, 2, 3],
    "b": {
        "e": [4, 5, 6],
    },
    "c": {
        "c": [7, 8, 9],
    },
}

my_dict_2 = {
    "Vali": None,
    "Ali": {
        {"Ballar": [40, 50, 60], }
    },
    "John": {
        "Ballar": [40, 50, 60],
        "email": "strin@asds",
        "family": {
            "father": {
                "name": "strin",
                "age": 22,
            },
            "mother": {
                "name": "strin",
                "age": 22,
            }
        }
    }
}

for key, value in my_dict.items():
    print(key, value)

students = {
    "Ferhad": {
        "age": 32,
        "height": 70,
        "weight": 80,
        "email": "<EMAIL>",
    },
    "Oguz": {
        "age": 25,
        "height": 70,
        "weight": 80,
        "email": "<EMAIL>",
    },
    "Vagif": {
        "age": 15,
        "height": 70,
        "weight": 85,
        "email": "<EMAIL>",
    },
    "Osman": {
        "age": 18,
        "height": 70,
        "weight": 80,
        "email": None,
    },
}

for key, value in students.items():
    if key == "Oguz":
        print(value["age"])

"""
None data tipi
"""

"""
Hansı vəziyyətlərdə hansını seçməliyik?

Tuple:
    Məlumatlar dəyişməz olmalı və sırası önəmli olduğu zaman. 
    Məsələn, koordinatlar, tarixlər, funksiya nəticələrinin qruplaşdırılması.
Set: 
    Təkrarlanmayan unikal elementlərin saxlanılması və ya hesablama əməliyyatlarının edilməsi lazım olduqda. 
    Məsələn, unikal dostlar, verilənlər üzərində kəsişmə əməliyyatı.
Dictionary: 
    Açar-dəyər cütləri ilə verilənlərin saxlanılması və tez bir şəkildə verilənlərə daxil olmaq lazım olduğunda. 
    Məsələn, istifadəçi məlumatları, məhsul kataloqu.
NoneType: 
    Heç bir dəyər göstərilmədikdə və ya funksiyaların heç bir nəticə qaytarmadığı zaman istifadə olunur. 
    Məsələn, funksiyaların geri dönüş növü yoxdur və ya başlanğıc dəyər olaraq None təyin edilir.
"""

"""
indiye qeder kecdiyimiz data tipleri:

int
float
str
bool
list
+
set
tuple
dict
None
"""

"""
Mutable (dəyişdirilə bilən), Immutable (dəyişdirilə bilməyən) Data tipləri

Mutable:
    - list
    - dict
    - set

Immutable:
    - int
    - float
    - str
    - bool
    - tuple

Dict'lərin keyləri mütləq immutable olmalıdır!
"""
