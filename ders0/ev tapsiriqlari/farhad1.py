name=input("Adiniz:")
surname=input("Soyadiniz:")
age=int(input("Yasiniz:"))
job=input("Peseniz:")
hobby1=input("Hobbiniz:")
hobby2=input("Hobbiniz:")
height=int(input("Boyunuz (sm ile):"))
weight=int(input("Cekiniz (kg ile)"))
bmi=height/(weight * weight)

print(f"Salam, sizin adınız {name} {surname} və {age} yaşınız var. Sizin peşəniz {job} və ən sevdiyiniz hobbi {hobby1} və {hobby2} oynamaqdır")
print(f"Bədən indeksiniz: {bmi}")