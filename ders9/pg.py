from datetime import datetime

start_time = datetime.now()

database = {
    '1': '1', '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    ' ': '0'
}

# Read the user's message
user_message = "ASLAKLJDLKASJDKAJSLKDJALKJDLKASJLDKJASLKDJLKASJDLKAJSLKDJLASKJDLKASJLDJALKDASJDLASJDKLJASLKDJALSKJDKAJLDJALDJ"

# Generate and display the key presses
key_presses = ""
for char in user_message:
    if char in database:
        key_presses = key_presses + database[char]
        break

print("Key presses:", key_presses)

print(datetime.now() - start_time)
# 0:00:00.000120
# 0:00:00.000056