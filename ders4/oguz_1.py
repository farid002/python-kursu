"""
Istifadəçidən 0 la 100 arasında tam ədəd daxil etməsini istəyin. Bu aralıqda olmazsa, bu ədəd 0-100 arasında tam
ədəd deyil deyib dəyəri yenidən almağa cəhd etsin. QEYD: dəyər istənilən kimi olana qədər istifadəçidən dəyəri
almağa cəhd göstərməlidir və bu zaman proqram sonlanmamalıdır.

Alınan dəyərə qədər olan bütün 3-ə, 5-ə, 3-ə və 5-ə tam bölünən ədədləri ayrı ayrı göstərin. Yəni əvvəlcə
3ə bölünən, sonra 5ə, sonra hər ikisinə bölünən ədədlər.

Təqribi çıxış belə olmalıdır:
0-100 arasında
3-ə bölünən ədədlər: 3, 6, 9, 12 ...
    5-ə bölünən ədədlər: 5, 10, 15, 20, 25 ...
    3-ə və 5-ə bölünən ədədlər: 15, 30, 45 ...
"""

while 1==1:
    a = int(input(f"0 la 100 arasında tam ədəd daxil edin\n"))
    if (a < 0 or a > 100):
        print("Tam ədəd deyil")
        continue
    else:
        break
"""
uce_bolunen = []
bese_bolunen = []
ikisinede_bolunen = []
"""
print("3e bölünen ededler: ")
for a in range(0, a+1, 3):
    print(a, end=" ")
print("\n5e bölünen ededler: ")
for a in range(0, a+1, 5):
    print(a, end=" ")
print("\n3e ve 5e bölünen ededler: ")
for a in range(0, a+1, 15):
    print(a, end=" ")