"""
Bir list yaradın, içində n ədəd tam sayı olsun. Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""

num_string_list = input("Please enter integers (doesn't matter how many):\n")

new_integers = list(num_string_list.split(','))

list_integers = []

for i in new_integers:
    i = int (i)
    if i % 2 == 0:
        new_integer = i // 2
    else:
        new_integer = i * 3 + 2
        list_integers.append(new_integer)


print(f"What you entered: {new_integers}")
print(f"Your answer is: {list_integers}")
