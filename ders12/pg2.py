from datetime import datetime

start = datetime.now()

def mükemmel_eded(n):
    summa = 0
    for i in range(1, n // 2 +1):
        if n % i == 0:
            summa += i
    return summa == n

for num in range(1, 100000):
    if mükemmel_eded(num):
        print(num)


print(datetime.now() - start)
