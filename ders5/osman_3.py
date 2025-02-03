"""İstifadəçidən bir tam ədəd (n) alın və 1-dən n-ə qədər bütün sadə ədədləri tapıb çap edin.
Qeyd: n 0-la 100 arasında olmalıdır.

Sadə ədəd yalnız 1-ə və özünə bölünən ədəddir."""
n = int(input("(0-100) qeder reqem secin"))
if 0 <= n <= 100:
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)): print(num, end=" ")
else:
    print("sefdi reqem 0 -100 qeder olmalidir")