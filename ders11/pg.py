def is_anagram(a,b):
    if len(a) == len(b):
        letter_count_a = {} # adam
        letter_count_b = {} # madam

        for letter in a:
            if letter not in letter_count_a:
                letter_count_a[letter] = 1
            else:
                letter_count_a[letter] += 1

        for letter in b:
            if letter not in letter_count_b:
                letter_count_b[letter] = 1
            else:
                letter_count_b[letter] += 1

        if letter_count_a == letter_count_b:
            return True
        else:
            return False
    else:
        return False


def is_anagram_2(a, b):
    for letter in a:
        if letter in b:
            b = b.replace(letter, "", 1)
        else:
            return False

    if b == "":
        return True
    else:
        return False

def is_anagram_3(a, b):
    for letter in a:
        if a.count(letter) != b.count(letter):
            return False
    for letter in b:
        if a.count(letter) != b.count(letter):
            return False
    return True




if __name__ == "__main__":
    print(is_anagram_3("madama", "madamat"))

