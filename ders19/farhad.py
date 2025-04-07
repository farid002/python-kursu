try:
    user_input = input("Enter filename: ")
    with open (user_input, "r", encoding='utf-8') as file:
        my_file = file.read()
        print(my_file)
except FileNotFoundError as e:
    print("File not found", e)