glass = int(input("Shushe qabların sayı:"))
plastik = int(input("Plastik qabların sayı:"))
a = 0.08   # constant boyukle
b = 0.25

float_a = float(a)
float_b = float(b)

sum = (glass * a) + (plastik * b)

print(f"Cəmi qaytarılacaq məbləğ - {sum}€")