"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""
ad_iste = input("Ad yazin")
try:
    with open(ad_iste, "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("file tapilmadi", e)

print(2+2)