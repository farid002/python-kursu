bir = input("Birinci sozunuzu daxil edin:\n").upper()
iki = input("Ikinci sozunuzu daxil edin:\n").upper()
elifba = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
netice = ""
say1 = 0
say2 = 0
if len(bir) == len(iki):
    for herf in bir:
        if herf not in iki:
            netice = "Anagram deyil"
            break
        else:
            netice = "Anagramdir"
    for herf in bir:
        indeks = elifba.index(herf)
        say1 += indeks
    for herf in iki:
        indeks = elifba.index(herf)
        say2 += indeks
    if say1 == say2:
        print("Anaqramdır")
    else:
        print("Anaqram deyil")
else:
    print("Anagram deyil")
# print(netice)