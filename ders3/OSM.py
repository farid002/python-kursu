#10 -10 sayli tam orta elementli siyahi yaradilir
my_mix_list = [10, 10, 15, 20, 5, 30, 25, 40, 35, 50]

#listin uzunlugunu cap edin
uzunluq = len(my_mix_list)
print("my_mix_listin uzunlugu:", uzunluq)

#siyahini bözükden kiciye siralayin
siralanmis_siyahi = sorted(my_mix_list, reverse=True)
print(siralanmis_siyahi)

# en böyük elementi tap
en_boyuk = max(my_mix_list)
print("en böyük element:", en_boyuk)