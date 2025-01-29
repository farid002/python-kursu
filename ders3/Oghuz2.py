"""
Istifadəçidən 0 la 100 arasında tam ədəd daxil etməsini istəyin. Bu aralıqda olmazsa, bu ədəd 0-100 arasında tam
ədəd deyil deyib dəyəri yenidən almağa cəhd etsin. QEYD: dəyər istənilən kimi olana qədər istifadəçidən dəyəri
almağa cəhd göstərməlidir və bu zaman proqram sonlanmamalıdır.

Alınan dəyərə qədər olan bütün 3-ə, 5-ə, 3-ə və 5-ə tam bölünən ədədləri ayrı ayrı göstərin.

Təqribi çıxış belə olmalıdır
"""
a = int(input(f"0 la 100 arasında tam ədəd daxil edin\n"))
if a < 0 or a > 100:
    print("Tam ədəd deyil")
else:
    for a in range(0, a, 3):
        print(a)
    for a in range(0, a, 5):
        print(a)
