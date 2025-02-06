"""
Tapşırıq:
Sizə tələbə adlarının və onların ballarının olduğu siyahı verilir. Sizdən tələb olunur:

1- enumerate() istifadə edərək: Hər tələbənin adını, balını və siyahıdakı mövqeyini (1-dən başlayaraq) çap edin
- hər tələbə məlumatı 1 sətirdə

2- Siyahı anlayışı (List Comprehension) istifadə edərək: Yalnız 50 və ya daha çox bal toplayan
tələbələrin adlarını verən yeni bir siyahı yaradın və sonda keçən tələbələr olaraq
adlarını və ballarını çap edin.

3- Bütün tələbələrin orta balını hesablayın.

4- Ən çox bal yığan tələbənin adını, balını və list indeksini göstərin (0-dan başlayaraq).
"""
students = ["Ali", "Farhad", "Oghuz", "Osman", "Vagif", "Farid", "Elvin", "Akbar"]
notes = [30, 85, 82, 93, 85, 35, 27, 80]

for index, student in enumerate(students):
    print(f"{index + 1}. {student}-{notes[index]}")

# passed_students = []
#
# for note in notes:
#     if note >= 50:
#         print("You passed")
#     else:
#         print("You failed")
passed_students = [students[index] for index, note in enumerate(notes) if note >= 50]
print("Keçən tələbələr:", passed_students)


average_score = sum(notes) / len(notes)
print(f"Orta bal: {average_score}")

max_score = max(notes)
print(f"En cox bal: {max_score}")

