"""
İstifadəçidən bir tam ədəd (n) alın və 1-dən n-ə qədər bütün sadə ədədləri tapıb çap edin.
Qeyd: n 0-la 100 arasında olmalıdır.

Sadə ədəd yalnız 1-ə və özünə bölünən ədəddir.
"""


n = int(input("0 ilə 100 arasında olmaq şərti ilə bir tam ədəd daxil edin:\n"))

if n<0 or n>100:
    print("Xahiş olunur, ədəd 0 ilə 100 arasında olmalıdır.")
else:
    primes = []

    for num in range(2, n+1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

            if is_prime:
                primes.append(num)

print(primes)
