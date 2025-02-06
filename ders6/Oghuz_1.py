"""
Tapşırıq:
Sizə tələbə adlarının və onların ballarının olduğu siyahı verilir. Sizdən tələb olunur:

1- enumerate() istifadə edərək: Hər tələbənin adını, balını və siyahıdakı mövqeyini (1-dən başlayaraq) çap edin
- hər tələbə məlumatı 1 sətirdə

2- Siyahı anlayışı (List Comprehension) istifadə edərək: Yalnız 50 və ya daha çox bal toplayan
tələbələrin adlarını və ballarını çap edin.

3- Bütün tələbələrin orta balını hesablayın.

4- Ən çox bal yığan tələbənin adını, balını və list indeksini göstərin (0-dan başlayaraq).
"""
students = ["Ali", "Farhad", "Oghuz", "Osman", "Vagif", "Farid", "Elvin", "Akbar"]
notes = [30, 85, 82, 93, 85, 35, 27, 80]
for index, student in enumerate(students):
    print(f"{index+1}. {student} - {notes[index]}")
print("---------------------------------")
elliden_cox_bal_toplayanlar = [print(note,"-", students[index]) for index, note in enumerate(notes) if note >= 50]

print("---------------------------------")

orta_bal = sum(notes)/len(notes)
print(f"Orta bal:{orta_bal}")

print("---------------------------------")


en_cox_bal = max(notes)
en_cox_balin_indexi = notes.index(en_cox_bal)
en_cox_bal_yigan = students[en_cox_balin_indexi]
print(f"En cox bal yigan telebe:\n{en_cox_balin_indexi}. {en_cox_bal_yigan}-{en_cox_bal}")