fayl_adi = input("fayilin adini daxil edin:")

try:
    print(open(fayl_adi, encoding="utf-8").read())
except FileNotFoundError as e:
    print("bele fayl adi tapilmadi", e)
print(2 + 2)