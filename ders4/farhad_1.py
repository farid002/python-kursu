while True:
    num = int(input("0-100 arasinda regem daxil edin: "))
    if 0 <= num <= 100:
        print("3e bölünen ededler: ")
        for i in range(0, num + 1):
            if i % 3 == 0:
                print(i)

        print("5e bölünen ededler: ")
        for i in range(0, num + 1):
            if i % 5 == 0:
                print(i)

        print("3e ve 5e bölünen ededler: ")
        for i in range(0, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print(i)
        break
    else:
        print("Bu ədəd 0-100 arasında tam ədəd deyil. Yenidən cəhd edin.")

