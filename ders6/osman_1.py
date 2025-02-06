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

for index, student in enumerate(students,1):
    print(f"{index}. {student} - ballar: {notes[index-1]}")

high_scorers = [print(students[i], notes[i]) for i in range(len(notes)) if notes[i] >= 50]
"""
print("\nStudentler hansici 50 ve cox ball yixanlar:")
for score in high_scorers:
    print(f"{students} - ballar: {score}")
"""
avarage_score = sum(notes) / len(notes)
print(f"\nOrta ball: {avarage_score:.15f}")

max_score_index = notes.index(max(notes))
print(f"\nStudent en böyök balla: {students[max_score_index]} - ballar: {notes[max_score_index]} - Indeks: {max_score_index}")