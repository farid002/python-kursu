"""
Morse code is an encoding scheme that uses dashes and dots to represent numbers
and letters. In this exercise, you will write a program that uses a dictionary to store
the mapping from letters and numbers to Morse code. Use a period to represent a dot,
and a hyphen to represent a dash. The mapping from letters and numbers to dashes
and dots is shown in Table 6.1.
Your program should read a message from the user. Then it should translate each
letter and number in the message to Morse code, leaving a space between each
sequence of dashes and dots. Your program should ignore any characters that are not
letters or numbers. The Morse code for "Hello, World!" is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..
"""

"""
Letter Code Letter Code Letter Code Number Code
A .- 
J .- - - 
S ... 1 .- - - -
B -... K -.- T - 2 ..- - -
C -.-. L .-.. U ..- 3 ...- -
D -.. M - - V ...- 4 ....-
E . N -. W .- - 5 .....
F ..-. O --- X -..- 6 -....
G - -. P .- -. Y -.- - 7 - -...
H .... Q - -.- Z - -.. 8 - - -..
I .. R .-. 0 ----- 9 - - - -.
"""
def text_to_morse(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".----",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".-.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }

    text = text.upper()
    return " ".join(morse_code[char] for char in text if char in morse_code)

user_input = input("Enter a message: ")
print("Morse code:", text_to_morse(user_input))

"""def text_to_morse(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".----",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".-.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    
    text = text.upper()
    morse_message = " "
    
    for char in text:
        if char in morse_code:
            morse_message += morse_code[char] + " "
            
    return morse_message.strip()
    
user_input = input("Enter a message: ")
print("morse code:")
print(text_to_morse(user_input))
"""