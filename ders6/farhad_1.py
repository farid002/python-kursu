students = ["Ali", "Farhad", "Oghuz", "Osman", "Vagif", "Farid", "Elvin", "Akbar"]
notes = [27, 93, 30, 93, 85, 35, 27, 80]

#1
for index, name in enumerate(students):
    print(index, name, notes[index])

print("")
#2
passing_students = [print(index, students[index], note) for index, note in enumerate(notes) if note >= 50]

print("")

#3
score = [print(f"Orta bal: {sum(notes) / len(notes)}")]


print("")

#4
index = notes.index(min(notes))
max_student = students[index]
max_score = notes[index]
print(f"En cox bal yigan telebe: {max_student}, Bal: {max_score}, İndeksi: {index}")