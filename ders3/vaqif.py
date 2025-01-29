#
# 10 integer elementli bir list təyin edin.
#     - Listin uzunluğunu çap edin
#     - Listi böyükdən kiçiyə sıralayın
#     - Ən böyük və kiçik ədədi çap edin
#



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(my_list))
my_list.sort(reverse=True)
print(my_list)
print(f"Largest number:{my_list[0]} and the smallest{my_list[-1]}")