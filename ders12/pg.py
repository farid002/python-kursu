from datetime import datetime

start = datetime.now()

def perfect_finder(num):
    if num <= 1:
        return False
    div_sum = 1

    for i in range(2, num):
        if num % i == 0:
            div_sum += i

    return div_sum == num

for num in range(1, 100000):
    if perfect_finder(num):
        print(num)

print(datetime.now() - start)


