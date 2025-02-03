"""
Döngüdən istifadə edərək 0-dan 100-ə qədər olan tam ədədlərdən:
5-ə tam bölünən ədədləri
15-ə tam bölünən ədədləri
Kvadratı 50 və 200 arasında olan tam ədədləri (böyükdən kiçiyə sıralı)
çap edin (terminala yazdırın)

İpucular:
Əvvəlcə for-un çölündə boş list(lər)inizi təyin edin. Məs: beshe_bölünən_ədədlər = []
for döngüsünün içində .append() funksiyasından istifadə edərək həmin listlərə dəyərlər əlavə edin (əlbəttə if, else ve ya elif istifadə edərək kontrol etməlisiniz)
for döngü bloklarının içində if-else-elif və digər öyrəndiyimiz bilgiləri istifadə edə bilərsiniz
köməklik edəcək bəzi açar sözlər: for, if, else, elif, reverse, append, print, range

"""

# Bosh listlerin yaradilmasi
beshe_bolunen_ededler = []
onbeshe_bolunen_ededler = []
kvadrati_araliqda_olanlar = []

# 0-dan 100-e qeder olan tam ededlerin yoxlanilmasi
for eded in range(101):
    if eded % 5 == 0:
        beshe_bolunen_ededler.append(eded)
    if eded % 15 == 0:
        onbeshe_bolunen_ededler.append(eded)
    if 50 <= eded ** 2 <= 200:
        kvadrati_araliqda_olanlar.append(eded)

# Kvadratları 50-200 arasinda olanlari böyükden kiciye siralamaq
kvadrati_araliqda_olanlar.sort(reverse=True)

# Neticelerin cap olunmasi
print("5-ə tam bölünən ədədlər:", beshe_bolunen_ededler)
print("15-ə tam bölünən ədədlər:", onbeshe_bolunen_ededler)
print("Kvadratı 50 və 200 arasında olan tam ədədlər (böyükdən kiçiyə):", kvadrati_araliqda_olanlar)






