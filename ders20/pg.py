total_sum = 0

try:
    with open ("reqemler.txt", "r",  encoding='utf-8') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("File is empty!")
        try:
            total_sum = sum(map(int, lines))
        except ValueError:
            print(f"Səhv məlumat tapıldı!")
        else:
            print(f"Total sum: {total_sum}")
except FileNotFoundError:
    print("File not exist")
finally:
    print("Program is finished.")