"""
10 integer elementli bir list təyin edin.
    - Listin uzunluğunu çap edin
    - Listi böyükdən kiçiyə sıralayın
    - Ən böyük və kiçik ədədi çap edin
    -
"""
my_mixed_list = [12, 15, 1556, 1, -5.14, 323434, 34344, 1234, 348, 924]
print(len(my_mixed_list))
my_mixed_list.sort(reverse=True)
my_length = len(my_mixed_list)
print(my_length) #sehvimi tutmadim, burda sehvim nededi?
print(max(my_mixed_list))
print(min(my_mixed_list))
#aha, tamamdir