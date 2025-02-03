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

for element in range(0, 101, 5):
    print(element, end=" ")
print("\n")
for element in range(0, 101, 15):
    print(element, end=" ")
print("\n")
for element in range(100, -1, -1):
    if 50 <= element**2 <= 200:
        print(element, end=" ")