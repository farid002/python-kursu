##########################################################################################
#########################   YALNIZ BU HİSSƏNİ DƏYİŞİN   ##################################

"""
Aşağıdakı "eded" dəyişkənin dəyəri hazırda 0-a bərabərdir.
həmin sətrə dəyişiklik edərək "eded" dəyişkənini int(input("")) vasitəsilə
istifadəçidən alın. İstifadəçiyə 100-ə qədər hər hansı 1 tam ədəd daxil etməsini deyin
"""

eded = int(input("1-100 geder 1 regem daxil edin:"))

###########################################################################################
###########################################################################################

sade_olmagi = True
for i in range(2, eded):
    if eded % i == 0:
        sade_olmagi = False
        break

sade_eded_sayi = 0
kicik_olan_sade_ededler = []

for i in range(2, eded):
    sadelik = True
    for j in range(2, i):
        if i % j == 0:
            sadelik = False
            break
    if sadelik:
        sade_eded_sayi += 1
        kicik_olan_sade_ededler.append(i)

# Task 4: Print the results (prime check, prime count, and list of primes)
if sade_olmagi:
    print(f"Daxil edilmiş ədəd sadə ədəddir.")
else:
    print(f"Daxil edilmiş ədəd sadə ədəd deyil.")

##########################################################################################
#########################   YALNIZ BU HİSSƏNİ DƏYİŞİN   ##################################

"""
Bu hissədə isə print() funksiyasından istifadə edərək:

Daxil edilən rəqəmin dəyərini - eded
Həmin dəyərdən kiçik neçə sadə ədəd var - sade_eded_sayi
Həmin dəyərdən kiçik sadə ədədlər hansılardır - kicik_olan_sade_ededler

Kodunuzu aşağıdakı 3 dırnağın altından, print funksiyasından əvvəl yazın.
"""
print(f"Daxil edilən ədədin dəyəri: {eded}")
print(f"Həmin dəyərdən kiçik neçə sadə ədəd var: {sade_eded_sayi}")
print(f"Həmin dəyərdən kiçik sadə ədədlər: {kicik_olan_sade_ededler}")

print("Qeyd: 1 nə sadə, nə də mürəkkəb ədəddir!")
##########################################################################################
##########################################################################################