"""
İstifadəçidən bir tam ədəd (n) alın və 1-dən n-ə qədər bütün sadə ədədləri tapıb çap edin.
Qeyd: n 0-la 100 arasında olmalıdır.

Sadə ədəd yalnız 1-ə və özünə bölünən ədəddir.
"""
a = int(input(f"Eded daxil edin"))
if a < 1 or a > 100:
    print("Duzgun eded daxil edin")
else:
    print("Verdiyiniz eded secildi")
    for number in range(2, a+1, 1):
        if number % number == 0 and number % 1 == 0:
            for bolunen in range(2, number, 1):
                if number % bolunen == 0:
                    break
            else:
                print(number, end=" ")