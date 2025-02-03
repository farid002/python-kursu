"""
Bir list yaradın, içində n ədəd tam sayı olsun.
Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""


my_list1 = [32, 34, 56, 13 ,8, 24, 46, 50]
my_list2 = []
for i in my_list1:
    if i % 2 == 0:
        my_list2.append(i/2)
    else:
        my_list2.append((i*3)+1)
print(my_list2)
