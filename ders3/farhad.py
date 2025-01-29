# 10 integer elementli bir list təyin edin.
numbers = [20, 303, 50, 15, 22, 7, 45, 6, 9, 10]

# Listin uzunluğunu çap edin
print(f"Listin uzunlugu: {len(numbers)}")

# Listi böyükdən kiçiyə sıralayın
numbers.sort(reverse=True)
print(f"Böyükden kiciye siralanma: {numbers}")

# Ən böyük və ən kiçik ədədi çap edirik
largest = max(numbers)
smallest = min(numbers)
print("En böyük eded:", largest)
print("En kicik eded:", smallest)