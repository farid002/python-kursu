"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır).
"""

"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""
from vagif import factorial
"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""

"""
Tapşırıq 4: main() funksiyası yazım, hansı ki 3 parameter, ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
#1
def salamlamaq(name):
    print(f"salam {name}!")

#2
def cem(a, b, c):
    return a + b + c

#4
def main(name, a, b, c):
    salamlamaq(name)
    menim_cemi = cem(a, b, c)
    menim_faktoriyal = factorial(menim_cemi)
    return menim_cemi, menim_faktoriyal

if __name__ == '__main__':
    name_input = input("Adinizi yazin")
    a_input = int(input("Eded yazin"))
    b_input = int(input("Eded yazin"))
    c_input = int(input("Eded yazin"))
    print(main(name_input, a_input, b_input, c_input))
