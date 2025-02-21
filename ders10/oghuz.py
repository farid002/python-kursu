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

def salamla(ad):
    print(f"Necesen {ad}?")

def iki_ededin_cemi (a, b):
    return a + b

def factorial(n):
    fakt = 1
    for a in range(1, n+1):
        fakt = fakt * a
    return fakt

def main(ad, int1, int2):
    salamla(ad)
    my_sum = iki_ededin_cemi(int1, int2)
    my_fact = factorial(my_sum)
    return my_sum, my_fact

if __name__ == "__main__":
    ad = input("Ad yazin:\n")
    int1 = int(input("Int1 yazin:\n"))
    int2 = int(input("Int2 yazin:\n"))
    my_sum_output, my_fact_output = main(ad, int1, int2)
    print(f"Sum: {my_sum_output}, Fact: {my_fact_output}")