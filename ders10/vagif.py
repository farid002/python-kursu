"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır).
"""

"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""

"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""

"""
Tapşırıq 4: main() funksiyası yazım, hansı ki 3 parameter, ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""


# name_input = input("Enter the name you want to greet:\n")

def greet(name):
    print("Hello, " + name)

# greet(name_input)


# in1 = int(input("Enter the first integer: "))
# in2 = int(input("Enter the second integer: "))

def calculation(num1, num2):
    return num1 + num2
# calculation(in1, in2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_while(n):
    fact_result = 1
    while n > 0:
        fact_result = fact_result * n
        n = n - 1
    return fact_result

#n = int(input("Enter a number to calculate its factorial: "))
#print(f"The factorial of {n} is {factorial(n)}")

def main():
    name_input = input("Enter the name you want to greet:\n")
    greet(name_input)

    in1 = int(input("Enter the first integer: "))
    in2 = int(input("Enter the second integer: "))
    sum_result = calculation(in1, in2)
    print(f"The sum of {in1} and {in2} is {sum_result}")

    factorial_result = factorial_while(sum_result)
    print(f"The factorial of {sum_result} is {factorial_result}")

if __name__ == "__main__":
    main()