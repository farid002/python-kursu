"""
Bu tapşırıqda siz istifadəçilərin kontakt məlumatlarını saxlayan, idarə edən və axtarış edə bilən bir Python proqramı hazırlayacaqsınız.
Proqram kontaktları faylda saxlayacaq və istifadəçi ilə interaktiv işləyəcək.

-------Yeni kontakt əlavə et
İstifadəçidən ad, telefon nömrəsi və e-poçt ünvanını daxil etməyi tələb edin.
Bu məlumatları contacts.txt faylına "a" rejimində əlavə edin.
Hər əlaqə yeni sətirdə saxlanmalıdır:Ad: Elvin, Telefon: +994501234567, E-poçt: elvin@example.com

-------Bütün kontaktları göstər
contacts.txt faylındakı bütün əlaqələri oxuyub ekrana çıxarın.
Əgər fayl mövcud deyilsə və ya boşdursa, uyğun mesaj göstərin.

-------Kontakta görə axtarış et
İstifadəçidən bir ad və ya telefon nömrəsi daxil etməsini istəyin.
contacts.txt faylını oxuyaraq uyğun gələn kontaktı tapıb göstərməlidir.
Əgər uyğun kontakt tapılmazsa, mesaj verin:Bu adda kontakt tapılmadı!

-------Kontaktı sil
İstifadəçidən bir ad daxil etməsini istəyin.
Əgər həmin adla kontakt mövcuddursa, onu fayldan silin.
Əgər əlaqə tapılmazsa, uyğun mesaj göstərin.

İstifadəçi aşağıdakı seçimlərdən birini edə bilər:
1. Yeni kontakt əlavə et
2. Bütün kontaktları göstər
3. Kontakta görə axtarış et
4. Kontaktı sil
5. Çıxış
"""

def add_contact():
    name = input("Ad daxil edin: ")
    phone = input("Telefon daxil edin: ")
    email = input("Email daxil edin: ")

    with open("contacts.txt", "a") as file:
        file.write(f"Ad: {name}, Telefon: {phone}, Email: {email}\n")

"""
[Ad: Farhad, Telefon: +491654, Email: asdad@,
Ad: Oguz, Telefon: +4916422354, Email: asdad@,
Ad: Osman, Telefon: +2432, Email: asdad@,
Ad: Farid, Telefon: +49135654, Email: asdad@]
"""

def show_contacts():
    with open("contacts.txt", "r") as file:
        print(file.read())

def search_contact():
    search_text = input("Ad və ya telefon nömrəsi daxil edin\n")
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if search_text in line:
                print(line)

def delete_contact():
    name = input("Ad daxil edin: ")
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if name in line:
                lines.remove(line)

    with open("contacts.txt", "w") as file:
        file.write("".join(lines))


if __name__ == '__main__':
    while True:
        choice = int(input("1. Yeni kontakt əlavə et\n2. Bütün kontaktları göstər\n3. Kontakta görə axtarış et\n4. Kontaktı sil\n5. Çıxış\n"))
        if choice == 1:
            add_contact()
        elif choice == 2:
            show_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            break
        else:
            print("Verilən dəyər doğru deyil, zəhmət olmasa menyudan seçin:\n")
