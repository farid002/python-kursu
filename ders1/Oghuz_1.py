"""
Almaniyada insanları təkrar emal etməyə təşviq etmək üçün içki qablarına kiçik bir depozit əlavə olunur (Refund).

Şüşə içki qabları üçün 0,08 avro;
Plastik içki qabları üçün isə 0,25 avro depozit var.

Elə proqram yazın ki:
    - İstifadəçidən hər tipdə qabların sayını alsın
    - Həmin qabların qaytarılması üçün alınacaq pulu hesablayıb istfadəçiyə göstərsin.
    - Çıxışı elə formatlayın ki, avro işarəsi əlavə edilsin və məbləğdə həmişə iki onluq yer göstərilsin.

Məsələn:
Şüşə qabların sayı: ...
Plastik qabların sayı: ...

Cəmi qaytarılacaq məbləğ - 2.25 €
"""
suse = float(input("Suse qablarin sayini elave edin\n")) #suse sayi   # int olmali
plastic = float(input("Plastik qablarin sayini elave edin\n")) #plastik sayi
print(f"Suse qablarin sayisi: {suse} \nPlastik qablarin sayisi: {plastic}") #ikisinin sayilari
print(f"Suse qablarin qiymeti: {suse*0.08} \nPlastik qablarin qiymeti: {plastic*0.25}") #ikisinin qiymetleri
print(f"Cem qaytarilacak mbl: {(suse*0.08)+(plastic*0.25)}") #toplam qiymet

