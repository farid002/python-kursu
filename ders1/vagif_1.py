plastic_bottles = int(input('Value  plastic bottles: '))
glass_bottles = int(input('Value  glass bottles: '))

TAX_PLASTIC = 0.25
tax_glass = 0.08


total_tax_plastic = plastic_bottles * TAX_PLASTIC
total_tax_glass = glass_bottles * tax_glass

print(f"Toplam plastik: {plastic_bottles}\nToplam şüşə qab: {glass_bottles}\nToplam plastik qab vergisi: {total_tax_plastic}$\nToplam şüşə qab vergisi: {total_tax_glass}$")

print("Ümumi ödədiyiniz vergi: ", total_tax_plastic + total_tax_glass)