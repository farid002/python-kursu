while True:
    try:
        n = int(input("Enter a number between 0 and 100: "))
        if 0 <= n <= 100:
            break
        else:
            print("Number must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

simple_numbers = [1]
for x in range(1, n + 1):
    if x == 1:
        simple_numbers.append(x)
    else:
        is_simple = True

        x = 13

        for i in range(2, x ** 0.5 + 1):
            if x % i == 0:
                is_simple = False
                break
        if is_simple:
            simple_numbers.append(x)

print("Simple numbers from 1 to", n, "are:", simple_numbers)
