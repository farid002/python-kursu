"""
Istifadəçidən 0 la 100 arasında tam ədəd daxil etməsini istəyin. Bu aralıqda olmazsa, bu ədəd 0-100 arasında tam
ədəd deyil deyib dəyəri yenidən almağa cəhd etsin. QEYD: dəyər istənilən kimi olana qədər istifadəçidən dəyəri
almağa cəhd göstərməlidir və bu zaman proqram sonlanmamalıdır.

Alınan dəyərə qədər olan bütün 3-ə, 5-ə, 3-ə və 5-ə tam bölünən ədədləri ayrı ayrı göstərin. Yəni əvvəlcə
3ə bölünən, sonra 5ə, sonra hər ikisinə bölünən ədədlər.

Təqribi çıxış belə olmalıdır:
0-100 arasında:
    3-ə bölünən ədədlər: 3, 6, 9, 12 ...
    5-ə bölünən ədədlər: 5, 10, 15, 20, 25 ...
    3-ə və 5-ə bölünən ədədlər: 15, 30, 45 ...
"""

while True:
    num = int(input("0 - 100 qeder reqem yazin\n"))
    if 0 <= num <= 100:
        break
    else:
        print("Yanlış!", end=" ")

print("regemler hansi 3 bölünür:" , [i for i in range(1, num+1) if i % 3 == 0])
print("ededler hansi 5 bülönür:" , [i for i in range(1, num+1) if i % 5 == 0])
print("ededler hansi 5 ve 3 bölünür:", [i for i in range(1,num+1) if i % 3 == 0 and i % 5 == 0])